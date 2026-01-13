from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from Restaurant.models import Menu
from Restaurant.serializers import MenuSerialiazer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title='Crocodile ala creme',
            price=27,
            inventory=19
        )
        self.assertEqual(str(item), 'Crocodile ala creme : 27')


class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        Menu.objects.create(title="Burger", price=8.99, inventory=20)
        Menu.objects.create(title="Pasta", price=10.49, inventory=15)

    def test_getall(self):
        response = self.client.get('/restaurant/api/menu-items/')

        menus = Menu.objects.all()
        serializer = MenuSerialiazer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
