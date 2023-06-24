from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['appetizers', 'beverages', 'desserts', 'chefs_specials', 'date', 'restaurant']
