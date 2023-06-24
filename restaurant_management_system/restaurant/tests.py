from django.test import TestCase
from .models import Restaurant


class RestaurantModelTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Sample Restaurant',
            address='123 Main St',
            phone_number='123-456-7890',
            email='info@restaurant.com',
            description='A sample restaurant for testing purposes',
            opening_time='09:00',
            closing_time='21:00'
        )

    def test_restaurant_name(self):
        self.assertEqual(self.restaurant.name, 'Sample Restaurant')

    def test_restaurant_address(self):
        self.assertEqual(self.restaurant.address, '123 Main St')

    def test_restaurant_phone_number(self):
        self.assertEqual(self.restaurant.phone_number, '123-456-7890')

    def test_restaurant_email(self):
        self.assertEqual(self.restaurant.email, 'info@restaurant.com')

    def test_restaurant_description(self):
        self.assertEqual(self.restaurant.description, 'A sample restaurant for testing purposes')

    def test_restaurant_opening_time(self):
        self.assertEqual(self.restaurant.opening_time, '09:00')

    def test_restaurant_closing_time(self):
        self.assertEqual(self.restaurant.closing_time, '21:00')
