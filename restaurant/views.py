from rest_framework import generics, views, response
from rest_framework.permissions import IsAuthenticated
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer
from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer

def home(request):
  return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer