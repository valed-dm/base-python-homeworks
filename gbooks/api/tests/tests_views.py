from django.test import TestCase


class TestViews(TestCase):
    def test_book_search(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
