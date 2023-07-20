from django.test import TestCase
from .models import User, Mountain, Level, Coordinates, Images
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase


def create_mountain(self):
    """
    Create a mountain
    """

    return Mountain.objects.create(user=self.user, beauty_title='test',
                                   title='title-test', other_titles='other_title',
                                   levels=self.levels, coordinates=self.coordinates)


class ApiModelTest(TestCase):
    """
    Test models, create mountain
    """

    def setUp(self):
        # Setup run before every test method.
        self.user = User.objects.create(name='Vasily',
                                        last_name='Vasilievich',
                                        second_name='Morozov',
                                        email='user@example.com',
                                        phone='+1934592752')
        self.level = Level.objects.create(winter='ddd')
        self.coord = Coordinates.objects.create(latitude='12.721', longitude='456.128', height='252')
        self.image = Images.objects.create(title='Very best', image='null')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_setUpTestData(self):
        new = create_mountain(self)
        self.assertEqual(new.beauty_title, 'test')


class PersonViewSetTests(APITestCase):

    def test_list_mountain(self):
        """
        Test to list all the mountains in the list
        """

        url = 'http://127.0.0.1:8000%s' % reverse('list_or_create_mountain')

        response = self.client.get(url, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json), 4)
