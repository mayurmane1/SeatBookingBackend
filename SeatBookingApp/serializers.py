from rest_framework import serializers
from SeatBookingApp.models import *

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

class AddRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
    
class GetRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
        depth = 1
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class GetBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1