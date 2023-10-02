from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu, MenuItem
from .serializers import bookingSerializer, menuSerializer,MenuSerializer,MenuItemSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



def test(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request,'index.html',{})


class bookingview(APIView):
    def get(self, request):
        items=Booking.objects.all()
        serializer=bookingSerializer(items, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serlializer=bookingSerializer(data=request.data)

        if serlializer.is_valid():
            serlializer.save()
            return Response({"status":"success","data":serlializer.data})
        
class menuview(APIView):
    def get(self, request):
        items=Menu.objects.all()
        serializer=menuSerializer(items, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serlializer=menuSerializer(data=request.data)

        if serlializer.is_valid():
            serlializer.save()
            return Response({"status":"success","data":serlializer.data})
        
class MenuItemsView (generics.ListCreateAPIView):
    def get(self, request):
        items=Menu.objects.all()


class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer



class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer





        
    
