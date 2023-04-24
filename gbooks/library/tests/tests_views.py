from django.test import TestCase


class TestViews(TestCase):
    def test_library(self):
        response = self.client.get("/library/")
        self.assertEqual(response.status_code, 200)
