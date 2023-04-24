import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import TestCase
from django.test.client import RequestFactory

from api.schemas import Book
from api.views import books_view, book_view


class TestViews(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_book_search(self):
        request = self.factory.get('/')
        response = books_view(request)
        self.assertEqual(response.status_code, 200)

    def test_book_details(self):
        b = Book()
        # prepare a test book object to be stored in session
        b_dict = b.__dict__
        b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)
        b_key = "test_book"
        # stores serialized book object into session
        session = self.client.session
        session[b_key] = b_serialized
        # Create an instance of a GET request.
        request = self.factory.get('/book/?id=test_book')
        # 'WSGIRequest' object gets attribute 'session'
        request.session = session

        response = book_view(request)

        self.assertEqual(response.status_code, 200)
