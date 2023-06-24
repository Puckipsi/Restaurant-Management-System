"""
URL configuration for restaurant_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .restaurant.views import RestaurantView
from .employee.views import EmployeeView
from .menu.views import MenuView, VoteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), 
    
    path('api/restaurants/create/', RestaurantView.as_view(), name='create-restaurant'),
    path('api/restaurants/<int:restaurant_id>/', RestaurantView.as_view(), name='get_restaurant'),
    path('api/restaurants/<int:restaurant_id>/menus/today/', RestaurantView.as_view(), name='get_today_menu'),
    path('api/restaurants/<int:restaurant_id>/menus/', MenuView.as_view(), name='create_menu'),
    path('api/restaurants/<int:restaurant_id>/employees/', EmployeeView.as_view(), name='create_employee'),
    path('api/restaurants/<int:restaurant_id>/employees/', EmployeeView.as_view(), name='get_restaurant_employees'),
    path('api/restaurants/employees/<int:employee_id>/menu/vote/', VoteView.as_view(), name='vote_for_menu'),
    path('api/restaurants/<int:restaurant_id>/menus/voting-results/', VoteView.as_view(), name='voting-results'),

]
