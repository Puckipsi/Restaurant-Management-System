from django.test import TestCase
from datetime import date
from .models import Employee
from ..restaurant.models import Restaurant

class EmployeeModelTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Sample Restaurant',
            address='123 Main St',
            phone_number='123-456-7890',
            email='info@restaurant.com',
            description='A sample restaurant for testing purposes',
            opening_time='09:00',
            closing_time='21:00')
        
        self.employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            position='Waiter',
            date_of_birth=date(1990, 1, 1),
            salary=2000.00,
            restaurant=self.restaurant
        )
        
    def test_employee_string_representation(self):
        self.assertEqual(str(self.employee), 'John Doe')
