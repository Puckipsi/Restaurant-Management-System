from datetime import datetime, date
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestaurantSerializer
from .models import Restaurant
from ..menu.models import Menu
from ..menu.serializers import MenuSerializer


class RestaurantView(APIView):
    
    def get(self, request, restaurant_id: int):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, restaurant_id: int):
        try:
            today_menus = []
            today = date.today()
            menus = Menu.objects.filter(Q(weekday=today.weekday() + 1) & Q(date=today) & Q(restaurant_id=restaurant_id))
            for menu in menus:
                serializer = MenuSerializer(menu)
                today_menus.append(serializer.data)
            return Response(today_menus, status=status.HTTP_200_OK)
        except Menu.DoesNotExist:
            return Response({"error": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
