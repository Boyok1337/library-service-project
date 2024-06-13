from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from library.models import Book


class BookTest(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "cover": "HARD",
            "inventory": "5",
            "daily_fee": 2.99
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        url = reverse("library:book-list")
        data = {
            "title": "New Book",
            "author": "New Author",
            "cover": "SOFT",
            "inventory": "15",
            "daily_fee": 12.99
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")