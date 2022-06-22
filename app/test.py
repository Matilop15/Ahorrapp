from re import X
from django.test import TestCase, Client, RequestFactory
from django.core.management import call_command
import requests
from requests.structures import CaseInsensitiveDict

# Python
from http import HTTPStatus

# Models
from django.contrib.auth.models import User
from requests import request


class ApiTestCase(TestCase):
    """Test for Django Api"""
    def setUp(self):
        """Create a client"""
        self.c = Client()

    def test_is_ok_page_admin(self):
        """Test for admin page and redirections"""
        response = self.c.get('/api/admin')
        self.assertEqual(response.status_code, HTTPStatus(301))
        self.assertRedirects(response, '/api/admin/', status_code=301, target_status_code=302, fetch_redirect_response=True)

    def test_is_ok_page_product(self):
        """Test for prodict page and redirections"""
        response = self.c.get('/api/products/')
        #self.assertEqual(response.status_code, HTTPStatus(301))
        #self.assertRedirects(response, '/api/product/', status_code=301, target_status_code=200, fetch_redirect_response=True)

    def test_Api_Supermarkets(self):
        """All test for api/markets/"""
        url = "http://localhost:8000/api/markets/"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = '{"Name": "MAtitester", "url": "https://www.TEST.com.uy/"}'

        #POST METHOD
        post_error = b'{"detail":"Method \\"POST\\" not allowed."}'
        resp = requests.post(url, headers=headers, data=data)
        if HTTPStatus == 405:
            error = 405
        elif HTTPStatus == 400:
            error = 400
        else:
            error = HTTPStatus
        self.assertEqual(resp.status_code, error) #201 created #400 bad request  #405 method not allowed 
        
        data = '{}'
        resp = requests.post(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request, no data
        self.assertEqual(resp.content, post_error)
        
        #PUT METHOD
        #empty data
        put_error = b'{"detail":"Method \\"PUT\\" not allowed."}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request #201
        self.assertEqual(resp.content, put_error)
        #no empty data
        data = '{"Name": "MAtitester", "url": "https://www.TEST.com.uy/"}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request
        self.assertEqual(resp.content, put_error)

        #DELETE
        url = "http://localhost:8000/api/markets/3"
        data = '{}'
        delete_error = b'{"detail":"Method \\"DELETE\\" not allowed."}'
        resp = requests.delete(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405 denegado #204 YES DELETE, no content
        self.assertEqual(resp.content, delete_error)
        
    def test_api_product(self):
        """All test for api/products/"""
        url = "http://localhost:8000/api/products/"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = '{"price":61,"product_url":"https://www.TEST.com.uy/","update_date":"2022-06-21","product_id":1,"market_id":1}'
        
        #POST METHOD
        post_error = b'{"detail":"Method \\"POST\\" not allowed."}'
        resp = requests.post(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(400)) #201 created #400 denegado

        data = '{}'
        resp = requests.post(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request, no data
        self.assertEqual(resp.content, post_error)

        #PUT METHOD
        #empty data
        put_error = b'{"detail":"Method \\"PUT\\" not allowed."}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request #201
        self.assertEqual(resp.content, put_error)
        #no empty data
        #FALTA SLUG
        data = '{"price":61,"product_url":"https://www.TEST.com.uy/","update_date":"2022-06-21","product_id":1,"market_id":1}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request
        self.assertEqual(resp.content, put_error)

        #DELETE
        delete_error = b'{"detail":"Method \\"DELETE\\" not allowed."}'
        url = "http://localhost:8000/api/products/3"
        data = '{}'
        resp = requests.delete(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405 denegado #204 YES DELETE, no content
        self.assertEqual(resp.content, delete_error)

    def test_Api_product_list(self):
        """All test for api/products/"""
        url = "http://localhost:8000/api/product_list/"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = '{"id":1,"name":"Harina 0000 Cañuelas 1 Kg","img_url":"https://TEST.img","brand_id":405,"cat_id":1,"sub_id":1}'
        
        #POST METHOD
        post_error = b'{"detail":"Method \\"POST\\" not allowed."}'
        resp = requests.post(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(400)) #201 created #400 denegado

        data = '{}'
        resp = requests.post(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request, no data
        self.assertEqual(resp.content, post_error)

        #PUT METHOD
        #empty data
        put_error = b'{"detail":"Method \\"PUT\\" not allowed."}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request #201
        self.assertEqual(resp.content, put_error)
        #no empty data
        data = '{"name":"Harina 0000 Cañuelas 1 Kg","img_url":"https://TEST.img","brand_id":405,"cat_id":1,"sub_id":1}'
        resp = requests.put(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405denegado #400 bad request
        self.assertEqual(resp.content, put_error)

        #DELETE
        delete_error = b'{"detail":"Method \\"DELETE\\" not allowed."}'
        url = "http://localhost:8000/api/products/3"
        data = '{}'
        resp = requests.delete(url, headers=headers, data=data)
        self.assertEqual(resp.status_code, HTTPStatus(405)) #405 denegado #204 YES DELETE, no content
        self.assertEqual(resp.content, delete_error)
