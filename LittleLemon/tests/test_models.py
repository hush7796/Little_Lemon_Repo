from django.test import TestCase
from restaurant import models

class MenuItemTest(TestCase):
    def test_create_item(self):
        item = models.Menu.objects.create(title="TestItem", price=999, inventory=0)
        self.assertEqual(item.title, "TestItem")
        self.assertEqual(item.price, 999)
        self.assertEqual(item.inventory, 0)
