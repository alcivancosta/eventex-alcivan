# coding: utf-8
from django.test import TestCase


class HomepageTest(TestCase):
    def test_get(self):
        'GET / must return status code 200.'
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
