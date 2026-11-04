from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from hotelapp.models import RoomDb,BookingDb
from hotelapp.serializers import RoomSerializer,BookingSerializer
from rest_framework import serializers
from datetime import datetime

class RoomListCreateView(APIView):
    def get(self,request):
        qs=RoomDb.objects.all()
        serializer_instance=RoomSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=RoomSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class RoomRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(RoomDb,id=pk)
        serializer_instance=RoomSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        room_object=get_object_or_404(RoomDb,id=pk)
        serializer_instance=RoomSerializer(room_object,data=form_data)   #serializer(instance= ,data= ,)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        room_object=get_object_or_404(RoomDb,id=pk)
        room_object.delete()
        return Response(data={
            "Message":"Deleted..."
        })

class BookingListCreateView(APIView):
    def get(self,request):
        qs=BookingDb.objects.all()
        serializer_instance=BookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=BookingSerializer(data=form_data)
        if serializer_instance.is_valid():
            #Get room_number, check_in_date, check_out_date to check whether the room is available or not
            room_no=serializer_instance.validated_data.get("room_number")
            check_in=serializer_instance.validated_data.get("check_in_date")
            check_out=serializer_instance.validated_data.get("check_out_date")
            
            # Check whether the room is already booked
            existing_booking=BookingDb.objects.filter(
                room_number=room_no,
                check_in_date__lt=check_out, #Checks whether the existing booking's check-in date is earlier than the new booking's check-out date.
                check_out_date__gt=check_in
                ).exists()
            
            if existing_booking:
                raise serializers.ValidationError("Room is already booked for these days")

            last_booking=BookingDb.objects.filter(
                room_number=room_no
                ).order_by("-booking_number").first()
            if last_booking is None:
                form_data["booking_number"]=1
            else:
                form_data["booking_number"]=last_booking.booking_number+1
            form_data["booking_time"]=datetime.now().time()

            qs=BookingDb.objects.create(**form_data)
            serializer_instance=BookingSerializer(qs)
            return Response(data={
                "Status":"Booking Successfull",
                "Booking_number":form_data["booking_number"],
                "Booking_time":form_data["booking_time"]
            })
        else:
            return Response(data=serializer_instance.errors)


# Existing booking: 5–8
# Case 1: New booking 8–10
# - Condition 1: 5 < 10 → True
# - Condition 2: 8 > 8 → False
# - Result: No overlap ✅ So booking allowed
# Case 2: New booking 1–4
# - Condition 1: 5 < 4 → False
# - Condition 2: 8 > 1 → True
# - Result: No overlap ✅ So booking allowed
# Case 3: New booking 6–8
# - Condition 1: 5 < 8 → True
# - Condition 2: 8 > 6 → True
# - Result: Overlap ❌ No booking allowed
# Case 4: New booking 6–9
# - Condition 1: 5 < 9 → True
# - Condition 2: 8 > 6 → True
# - Result: Overlap ❌ No booking allowed
# Case 5: New booking 4–6
# - Condition 1: 5 < 6 → True
# - Condition 2: 8 > 4 → True
# - Result: Overlap ❌ No booking allowed
# Case 6: New booking 5–8
# - Condition 1: 5 < 8 → True
# - Condition 2: 8 > 5 → True
# - Result: Overlap ❌ No booking allowed
# Case 7: New booking 8–12
# - Condition 1: 5 < 12 → True
# - Condition 2: 8 > 8 → False
# - Result: No overlap ✅ So booking allowed
# Case 8: New booking 1–5
# - Condition 1: 5 < 5 → False
# - Condition 2: 8 > 1 → True
# - Result: No overlap ✅ So booking allowed


class BookingRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        booking_object=get_object_or_404(BookingDb,id=pk)
        seralizer_instance=BookingSerializer(booking_object)
        return Response(data=seralizer_instance.data)
    
    def put(self,request,pk):
        form_data=request.data
        booking_object=get_object_or_404(BookingDb,id=pk)
        serializer_instance=BookingSerializer(booking_object,data=form_data)
        if serializer_instance.is_valid():
            room_no=serializer_instance.validated_data.get("room_number")
            check_in=serializer_instance.validated_data.get("check_in_date")
            check_out=serializer_instance.validated_data.get("check_out_date")

            existing_booking=BookingDb.objects.filter(
                room_number=room_no,
                check_in_date__lt=check_out,
                check_out_date__gt=check_in
            ).exclude(id=pk).exists()
            print("Room:", room_no)
            print("Check-in:", check_in)
            print("Check-out:", check_out)
            print("Conflict:", existing_booking)

            if existing_booking:
                raise serializers.ValidationError("Room is already booked for these days")
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
    def delete(self,request,pk):
        booking_object=get_object_or_404(BookingDb,id=pk)
        booking_object.delete()
        return Response(data={
            "Message":"Deleted successfully"
            })