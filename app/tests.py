from re import X
from django.test import TestCase, Client, RequestFactory
from django.core.management import call_command
# Python
from http import HTTPStatus

# Models
from django.contrib.auth.models import User

class ApiTestCase(TestCase):
    """Test for Django Api"""
    def setUp(self):
        """Create a client"""
        self.c = Client()

    def test_is_ok_page_admin(self):
        """Test for admin page and redirections"""
        response = self.c.get('/api/admin')
        self.assertEqual(response.status_code, HTTPStatus(301))
        self.assertRedirects(response, '/api/admin/', status_code=301,
                        target_status_code=302, fetch_redirect_response=True)

    def test_is_ok_page_product(self):
        """Test for prodict page and redirections"""
        response = self.c.get('/api/product')
        self.assertEqual(response.status_code, HTTPStatus(301))
        self.assertRedirects(response, '/api/product/', status_code=301,
                        target_status_code=200, fetch_redirect_response=True)
