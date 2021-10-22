import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class TestCreateUser(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.create_account = {
                "username": "mentee",
                "password": "Nepal@123",
                "password2": "Nepal@123",
                "email": "mentee@mentee.com",
                "role": "Mentee",
                "first_name": "fmentee",
                "last_name": "lmentee"
                }
        cls.client = APIClient()

    def test_register(self):
        data = json.dumps(self.create_account)
        resp = self.client.post('/api/register/', data=data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_register_failed(self):
        # username is made None which results to bad request
        self.create_account['username'] = None
        data = json.dumps(self.create_account)
        resp = self.client.post('/api/register/', data=data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
