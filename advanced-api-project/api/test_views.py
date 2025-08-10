from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test author
        self.author = Author.objects.create(name='Test Author')
        
        # Create test book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )
        
        # Authenticate client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # CRUD Operation Tests
    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_book_create(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update(self):
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_book_delete(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Filtering, Searching, Ordering Tests
    def test_book_filtering(self):
        Book.objects.create(
            title='Another Book',
            publication_year=2010,
            author=self.author
        )
        url = reverse('book-list')
        response = self.client.get(url, {'publication_year__gt': '2015'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_book_search(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_book_ordering(self):
        Book.objects.create(
            title='Another Book',
            publication_year=2010,
            author=self.author
        )
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    # Permission Tests
    def test_unauthenticated_access(self):
        self.client.logout()
        urls = [
            reverse('book-create'),
            reverse('book-update', args=[self.book.id]),
            reverse('book-delete', args=[self.book.id])
        ]
        for url in urls:
