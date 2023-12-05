from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ["title","price","inventory"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'