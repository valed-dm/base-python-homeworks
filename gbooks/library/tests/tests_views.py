import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import TestCase

from library.models import Book as DB_Book, Image


class TestViews(TestCase):
    def test_library(self):
        response = self.client.get("/library/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["width"], 105)
        self.assertEqual(response.context["height"], 150)

    def test_library_book(self):
        image_src = Image(image_src="/static/img/no_cover.webp")
        image_src.save()
        db_book = DB_Book(
            authors_str="test_author",
            title="test_title",
            description="test_description",
            date="1900-01-01",
            google_book_id="test_book",
            rubric="read_asap",
            image_src=image_src,
        )
        db_book.save()

        session = self.client.session
        session["auth"] = json.dumps("test_author", cls=DjangoJSONEncoder)
        session["cat-"] = json.dumps("test_category", cls=DjangoJSONEncoder)
        session.save()
        response = self.client.get('/library/book/test_book')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["width"], 150)
        self.assertEqual(response.context["height"], 210)
        self.assertTrue("library" in response.context)
        self.assertEqual(response.context["library"].all_authors, "test_author")
        self.assertEqual(response.context["library"].all_categories, "test_category")
