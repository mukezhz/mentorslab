from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status


USER = get_user_model()
class TestMentorMenteeFetch(APITestCase):
    @classmethod
    def setUpTestData(cls):
        USER.objects.create(
                username="user",
                email="user@user.com",
                first_name="uname",
                last_name="lname",
                role="Mentor"
                )
        USER.objects.create(
                username="user1",
                email="user1@user.com",
                first_name="uname1",
                last_name="lname1",
                role="Mentee"
                )
        cls.client = APIClient()

    def test_mentors(self):
        url = '/api/users/mentors/'
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(type(resp.json()), type([]))
        self.assertEqual(resp.json()[0]['username'], 'user')

    def test_mentees(self):
        url = '/api/users/mentees/'
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(type(resp.json()), type([]))
        self.assertEqual(resp.json()[0]['username'], 'user1')

    def test_get_single_user(self):
        url = '/api/users/user/'
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()['username'], 'user')
        url = '/api/users/user1/'
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()['username'], 'user1')
