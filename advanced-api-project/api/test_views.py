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

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Surrounded by Idiots',
            'publication_year': 2012,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'Surrounded by Idiots')

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication should fail"""
        data = {
            'title': 'Surrounded by Idiots',
            'publication_year': 2012,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication"""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'The Art of Public Speaking',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'The Art of Public Speaking')

    def test_update_book_unauthenticated(self):
        data = {
            'title': 'The Art of Public Speaking',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)

    def test_publication_year_validation(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'My Author Biography',
            'publication_year': 2030,  # Future year
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)

    def test_read_access_unauthenticated(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
