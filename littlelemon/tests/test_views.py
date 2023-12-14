from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name="Dish1", price=20, menu_item_description="Description 1")
        Menu.objects.create(name="Dish2", price=25, menu_item_description="Description 2")
        Menu.objects.create(name="Dish3", price=30, menu_item_description="Description 3")

        # Set up the client for making requests
        self.client = APIClient()

    def test_getall(self):
        # Retrieve all Menu objects
        url = reverse('menu-list')  # Assuming you have a URL pattern named 'menu-list'
        response = self.client.get(url)

        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)
        serialized_data = serializer.data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serialized_data)
