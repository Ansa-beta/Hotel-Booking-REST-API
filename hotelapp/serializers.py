from rest_framework import serializers
from hotelapp.models import RoomDb,BookingDb

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomDb
        fields="__all__"
        read_only_fields=["id"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingDb
        fields="__all__"
        read_only_fields=["id"]
        