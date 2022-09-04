from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, Category, Comment

User = get_user_model()


class CookBookTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.nonauth_client = Client()
        self.user = User.objects.create_user(
            username="test_user_1",
            email="test_1@ya.ru",
            password="test_123"
        )
        self.user2 = User.objects.create_user(
            username="test_user_2",
            email="test_2@ya.ru",
            password="test_123"
        )



    def test_index_code_200(self):
        response = self.client.get(reverse('index'))
        print(response)
        self.assertEqual(response.status_code, 200)
