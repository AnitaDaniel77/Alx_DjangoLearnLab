from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.book = Book.objects.create(
            title='Test Book',
            author='Author A',
            published_year=2020,
            price=150.00
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'Author B',
            'published_year': 2021,
            'price': 200.00
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'author': 'Author A',
            'published_year': 2022,
            'price': 180.00
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')
        self.assertEqual(response.data['published_year'], 2022)

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_filter_by_author(self):
        Book.objects.create(title='Another Book', author='Author B', published_year=2019, price=120.00)
        response = self.client.get(self.list_url + '?author=Author A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['author'], 'Author A')

    def test_search_by_title(self):
        response = self.client.get(self.list_url + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Test' in item['title'] for item in response.data))

    def test_order_by_published_year(self):
        Book.objects.create(title='Older Book', author='Author C', published_year=2010, price=100.00)
        response = self.client.get(self.list_url + '?ordering=published_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item['published_year'] for item in response.data]
        self.assertEqual(years, sorted(years))

