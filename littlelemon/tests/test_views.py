from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        t1 = Menu.objects.create(
            title = 'Tacos',
            price = '3',
            inventory = '500'
        )
        t2 = Menu.objects.create(
            title = 'Burgers',
            price = '5',
            inventory = '300'
        )
        t3 = Menu.objects.create(
            title = 'Salad',
            price = '4',
            inventory = '200'
        )
        
    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(serializer.data, response.data)