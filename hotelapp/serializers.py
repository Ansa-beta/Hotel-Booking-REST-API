from rest_framework import serializers
from hotelapp.models import RoomDb,BookingDb
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

        