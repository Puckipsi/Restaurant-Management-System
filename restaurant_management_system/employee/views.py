from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeView(APIView):
    
    def get(self, request, restaurant_id: int):
        employees = Employee.objects.filter(restaurant_id=restaurant_id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    def post(self, request, restaurant_id: int):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

