from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from SeatBookingApp.models import *
from SeatBookingApp.serializers import *
# Create your views here.

class AddSeats(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        try:
            data = Seat.objects.all().order_by('id')
            serialiser = SeatSerializer(data, many=True)
            return Response({'status': 200, 'data': serialiser.data, 'message': 'Data fetched successfully'})
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})
    
    def post(self, request):
        try:
            data = request.data
            serialiser = SeatSerializer(data=data)
            if serialiser.is_valid():
                serialiser.save()
                return Response({'status': 201, 'message': 'Seat added successfully'})
            else:
                return Response({'status': 400, 'message': 'Invalid data', 'errors': serialiser.errors})        
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})
    
class SelectSeats(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id):
        try:
            data = Seat.object.get(id=id)
            serialised_data = SeatSerializer(data)
            return Response({'data': serialised_data.data, 'status': 200, 'message': 'Data Fetched successfully'})
        except Seat.DoesNotExist: 
            return Response({'status': 404, 'message': 'Seat not found'})
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})
        
class AddCity(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            serializer = CitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 201, 'message': 'City added successfully'})
            else:
                return Response({'status': 400, 'message': 'Invalid data', 'errors': serializer.errors})
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})
    
    def get(self, request):
        try:
            data = Cities.objects.all()
            serializer = CitySerializer(data, many=True)
            return Response({'status': 200, 'data': serializer.data, 'message': 'Data fetched successfully'})
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})

class AddRoute(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            data = Routes.objects.all()
            serializer = AddRouteSerializer(data, many=True)
            return Response({'status': 200, 'data': serializer.data, 'message': 'Data fetched successfully'})
        except Exception as e:
            return Response({'status': 500, 'data': str(e), 'message': 'Internal Server Error'})

    def post(self, request):
        try:
            data = request.data
            route = Routes.objects.get(source_city__city=data['source_city'], destination_city__city=data['destination_city'])
            if route:
                return Response({'status': 400, 'data': 'Route already exists'})
            serializer = AddRouteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 201, 'message': 'Route added successfully'})
            else:
                return Response({'status': 400, 'message': 'Invalid data', 'errors': serializer.errors})
        except Exception as e:
            return Response({'status': 500, 'message': 'Internal Server Error', 'data': str(e)})

class GetRoute(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        data = Routes.objects.get(source_city=source, destination_city=destination)
        if data:
            serialized_data = GetRouteSerializer(data)
        else:
            return Response({'status': 404, 'message': 'No route found'})
        return Response({'status': 200, 'data': serialized_data.data, 'message': 'Data Fetched successfully'})

class Bookseat(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            route = Routes.objects.get(id=data['route'])
            if not route:
                return Response({'status': 400, 'data': 'Invalid route'})
            serialized_data = BookingSerializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response({'status': 200, 'data': serialized_data.data, 'message': 'Seat booked successfully'})
        except Exception as e:
            return Response({'status': 500, 'data': str(e), 'message': 'Internal Server Error'})
        

class GetBookingByRoute(APIView):
    permission_classes = [AllowAny]
    def get(self, request,routeId):
        try:
            data = Booking.objects.filter(route=routeId)
            serialized_data = GetBookingSerializer(data, many=True)
            return Response({'status': 200, 'data': serialized_data.data, 'message': 'Data fetched successfully'})
        except Booking.DoesNotExist:
            return Response({'status': 404, 'message': 'No booking found', 'data': []})
        except Exception as e:
            return Response({'status': 500, 'data': str(e), 'message': 'Internal Server Error'})
        
        