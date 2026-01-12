from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu ,  Booking
from .serializers import MenuSerialiazer , BookingSerialiazer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialiazer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialiazer


class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialiazer