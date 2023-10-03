from django.test import TestCase
from restaurant .models import Menu  # Import your Menu model here

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a Menu object
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        
        # Call the get_item method to get the string representation
        item_string = f"{item.title} : {item.price}"
       
        # Assert that the string representation matches the expected value
        self.assertEqual(item_string, "IceCream : 80")
