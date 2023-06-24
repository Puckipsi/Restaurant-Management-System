from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from restaurant_management_system.employee.models import Employee
from ..restaurant.models import Restaurant
from datetime import date



class Menu(models.Model):
    WEEKDAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
     
    weekday = models.PositiveSmallIntegerField(
        choices=WEEKDAY_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    appetizers = ArrayField(models.CharField(max_length=100),unique=True)
    beverages = ArrayField(models.CharField(max_length=100),unique=True)
    desserts = ArrayField(models.CharField(max_length=100),unique=True)
    chefs_specials = ArrayField(models.CharField(max_length=100),unique=True)
    date = models.DateField(blank=True, null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
 
    def get_menu_for_today(self):
        today = date.today()
        menu = Menu.objects.filter(date=today, restaurant=self).first()
        return menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=False)
 

