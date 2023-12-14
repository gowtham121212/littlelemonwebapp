from django.shortcuts import render
from .models import Menu, Booking, User
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# ... (your existing views)

def about(request):
    # Your view logic here
    return render(request, 'restaurant/about.html')

def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = BookingSerializer(bookings, many=True).data  # Use BookingSerializer
    return render(request, 'bookings.html', {"bookings": booking_json})

# ... (your existing views)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
            booking_json = BookingSerializer(booking).data  # Use BookingSerializer for the response
            return HttpResponse(booking_json, content_type='application/json')
        else:
            return HttpResponseBadRequest("{'error':1}", content_type='application/json')

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserListView(ListAPIView):
    queryset = User.objects.all()  # Assuming you have defined User model correctly in your models.py
    serializer_class = UserSerializer

class UserDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    # Your view logic here
    return render(request, 'restaurant/home.html')
class MenuItemsAPIView(APIView):
    def get(self, request):
        # Your API logic for handling GET requests
        return Response({'message': 'GET request handled'})

    def post(self, request):
        # Your API logic for handling POST requests
        return Response({'message': 'POST request handled'})