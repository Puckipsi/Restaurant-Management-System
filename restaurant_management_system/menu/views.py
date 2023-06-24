from django.db.models import Count
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import MenuSerializer
from .models import Vote

@authentication_classes([JWTAuthentication])
class MenuView(APIView):
    def post(self, request, restaurant_id):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
@authentication_classes([JWTAuthentication])
class VoteView(APIView):
    def post(self, request, employee_id):
        menu_id = request.data.get('menu_id')
        restaurant_id = request.data.get('restaurant_id')
        vote = Vote.objects.filter(employee=employee_id, restaurant_id=restaurant_id, menu_id=menu_id).first()
        
        if not vote:
            request.data.update({'employee_id':employee_id})
            Vote.objects.create(**request.data)
            return Response({'message': 'Vote counted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Vote already counted'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, restaurant_id):
        votes = []
        today = request.data.get("date")
        vote_counts = Vote.objects.filter(date=today, restaurant_id=restaurant_id).values('menu_id').annotate(total_votes=Count('id'))
        
        for vote in vote_counts:
            menu_id = vote['menu_id']
            total_votes = vote['total_votes']
            votes.append({"menu_id": menu_id, 'total_votes': total_votes})
 
        return Response(votes, status=status.HTTP_200_OK)