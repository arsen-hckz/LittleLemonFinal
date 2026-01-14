from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Menu ,  Booking
from .serializers import MenuSerialiazer , BookingSerialiazer
from rest_framework import generics,response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response('this is authenticated view')

def restaurant_home(request):
    return render(request, "index.html")

