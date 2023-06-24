from rest_framework import status
from rest_framework.response import Response
from .serializers import RestaurantSerializer
from .models import Restaurant
from rest_framework.views import APIView


class RestaurantView(APIView):
    
    def get(self, request, restaurant_id: int):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
