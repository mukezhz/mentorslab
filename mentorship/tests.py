from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status


USER = get_user_model()


class TestRequestApply(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = USER.objects.create(
                username="user",
                email="user@user.com",
                first_name="uname",
                last_name="lname",
                role="Mentor"
                )
        user.set_password("Nepal@123")
        user.save()
        user1 = USER.objects.create(
                username="mentee",
                email="mentee@mentee.com",
                first_name="uname",
                last_name="lname",
                role="Mentee"
                )
        user1.set_password("Nepal@123")
        user1.save()
        cls.url_token = reverse('token_obtain')
        cls.url_refresh = reverse('token_refresh')
        cls.credentials = {
                "email": "user@user.com",
                "password": "Nepal@123"
                }
        cls.data = {
            "title": "testing",
            "message": "testing this",
            "expectation": "test successful",
            "background": "django",
            "mentor_id": "user"
            }

    def test_apply_success(self):
        resp = self.client.post(self.url_token, self.credentials, format='json')
        access_token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Jwt {0}'.format(access_token))
        resp = self.client.post('/api/mentorships/apply/user/', data=self.data, format='json')
        stats = resp.json()['status']
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(stats, 'pending')

    def test_apply_failure(self):
        self.data['title'] = ''
        resp = self.client.post(self.url_token, self.credentials, format='json')
        access_token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Jwt {0}'.format(access_token))
        resp = self.client.post('/api/mentorships/apply/user/', data=self.data, format='json')
        title = resp.json()['title']
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(title[0], 'This field may not be blank.')

    def test_multiple_request(self):
        resp = self.client.post(self.url_token, self.credentials, format='json')
        access_token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Jwt {0}'.format(access_token))
        resp = self.client.post('/api/mentorships/apply/user/', data=self.data, format='json')
        message = resp.json().get('status')
        resp1 = self.client.post('/api/mentorships/apply/user/', data=self.data, format='json')
        message1 = resp1.json().get('mentor_id')[0]
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(message, 'pending')
        self.assertEqual(resp1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message1, 'Request already exists')
