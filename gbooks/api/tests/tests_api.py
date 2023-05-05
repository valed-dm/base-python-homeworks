import json
from unittest.mock import patch

from django.test import Client, TestCase
from django.urls import reverse

from api.api import fetch_to_session


class TestAPI(TestCase):
    client = Client()
    data = {
        "title": "test_book",
        "pace": "10",
        "category": "all",
        "sort": "relevance"

    }
    item = {
        "id": "test_id",
        "volumeInfo": {
            "authors": ["test_author"],
            "categories": ["test_category"],
            "publishedDate": "2023",
            "description": "test_description",
            "title": "test_book",
        }
    }

    @patch("api.api.fetch_books.fetch_data")
    def setUp(self, mock_request):
        mock_request.return_value = {
            "totalItems": 100,
            "items": [self.item]
        }
        response = self.client.post(reverse("books"), data=self.data)
        request = response.wsgi_request
        self.api = fetch_to_session(request)

    def test_fetch_to_session(self):
        # checks the main page view trigger
        self.assertEqual(self.api.display_start_info, False)
        # checks if books found qty number by api received
        self.assertEqual(self.api.books_found, 100)
        # checks if books incoming data processed properly
        self.assertEqual(self.api.books[0].authors, 'test_author')
        self.assertEqual(self.api.books[0].categories, 'test_category')
        self.assertEqual(self.api.books[0].date, '2023-01-01')
        self.assertEqual(self.api.books[0].description, 'test_description')
        self.assertEqual(self.api.books[0].google_book_id, 'test_id')
        self.assertEqual(self.api.books[0].image_src, '/static/img/no_cover.webp')
        self.assertEqual(self.api.books[0].title, 'test_book')
        self.assertEqual(self.api.books[0].rubric, 'read_asap')
        self.assertEqual(self.api.books[0].remark, '')
        # checks if test_book have been added to Django session
        self.assertEqual(
            json.loads(self.client.session['test_id'])['title'],
            'test_book'
        )
