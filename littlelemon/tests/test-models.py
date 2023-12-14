from django.test import TestCase
from .models import MenuItem  # Import your MenuItem model

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create an instance of the MenuItem model
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        
        # Call the get_item method and compare with the expected string
        expected_result = "IceCream : 80"
        self.assertEqual(item.get_item(), expected_result)
