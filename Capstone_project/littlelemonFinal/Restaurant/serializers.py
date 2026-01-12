from rest_framework import serializers
from .models import Menu, Booking


class MenuSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields  = "__all__"


class BookingSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields  = "__all__"