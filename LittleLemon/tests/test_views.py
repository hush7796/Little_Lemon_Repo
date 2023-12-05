from django.test import TestCase
from restaurant import models, serializers

class MenuViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.menu_test_item = models.Menu.objects.create(
            title="TestItem", 
            price=999, 
            inventory=0
        )

    def setUp(self):
        pass

    def test_get_item(self):
        item = models.Menu.objects.get(title="TestItem")
        self.assertEqual(item.title, "TestItem")
        self.assertEqual(item.price, 999)
        self.assertEqual(item.inventory, 0)


    def setUp(self):
        self.menu_test_item_2 = models.Menu.objects.create(
            title="TestItem2", 
            price=9999, 
            inventory=0
        )

    def test_get_all(self):
        items = models.Menu.objects.all()
        serialized_items = serializers.MenuItemSerializer(items, many=True)
        serialized_data = [dict(item) for item in serialized_items.data]
        data = [
            {"title": "TestItem", "price": "999.00", "inventory": 0},
            {"title": "TestItem2", "price": "9999.00", "inventory": 0}
        ]
        for dataitem in data:
            self.assertIn(dataitem, serialized_data)