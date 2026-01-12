from django.db import models

# Create your models here.
from django.utils import timezone


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField(default =  timezone.now)

    def __str__(self):
        return f"{self.name} ({self.booking_date})"
