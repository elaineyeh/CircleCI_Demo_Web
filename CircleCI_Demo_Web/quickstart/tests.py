from urllib import response
from django.test import TestCase


class TestHomePageCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/home/')

        self.assertEqual(response.status_code, 200)