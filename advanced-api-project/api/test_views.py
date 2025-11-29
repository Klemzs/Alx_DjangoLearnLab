from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name = "Nelson Mandela")
        self.book = Book.objects.create(
            title = "Long Walk to Freedom",
            publication_year = 1980,
            author = self.author
        )

        self.user = User.objects.create_user(
            username = 'ClementOdeh'
            password = '123456789'
        )

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Long Walk to Freedom')

    def test_retrieve_single_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Long Walk to Freedom')
        self.assertEqual(response.data['publication_year'], 1980)

    def test_create_book_authentication(self):
        self.client.force_authenticate(user=user.self)
        data = {
            'title': 'Surrounded by Idiots',
            'publication_year': 2012,
            'author': self.author.id
        }

