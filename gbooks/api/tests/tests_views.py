import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import Client
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from api.schemas import Book
from api.views import books_view, book_view


class SetUpTestData(TestCase):
    client = Client()
    session = client.session

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        b = Book()
        b.google_book_id = "LvEPas12H"
        # prepare a test book object to be stored in session
        b_dict = b.__dict__
        b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)
        b_key = "test_book"
        # stores serialized book object into session
        cls.session[b_key] = b_serialized


class TestViews(SetUpTestData):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_book_search(self):
        request = self.factory.get('/')
        response = books_view(request)
        self.assertEqual(response.status_code, 200)

    def test_book_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('book/?id=test_book')
        # 'WSGIRequest' object gets attribute 'session'
        request.session = self.session
        response = book_view(request)
        self.assertEqual(response.status_code, 200)

    def test_context_books(self):
        response = self.client.get("/")
        self.assertEqual("books" in response.context, True)
        self.assertEqual("books_found" in response.context, True)
        self.assertEqual("display_start_info" in response.context, True)
        self.assertEqual(response.context["width"], 105)
        self.assertEqual(response.context["height"], 150)

    def test_context_book(self):
        # self.session is not suitable for this test
        # client.get creates an empty session
        # api.helpers.get_book.py is modified for testing purpose
        # now url /book/ can be accessed and returns empty book example
        response = self.client.get(reverse(book_view))
        self.assertEqual("book" in response.context, True)
        self.assertEqual(response.context["width"], 150)
        self.assertEqual(response.context["height"], 210)
