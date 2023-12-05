from django.shortcuts import render
from django.contrib.auth.models import User 
from . import models, serializers
from rest_framework import generics, viewsets, permissions

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer