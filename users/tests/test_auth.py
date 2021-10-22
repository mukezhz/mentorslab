from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken ,RefreshToken


USER = get_user_model()


class TestAuthentication(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = USER.objects.create(
                username="user",
                email="user@user.com",
                first_name="uname",
                last_name="lname",
                )
        user.set_password("Nepal@123")
        user.save()
        cls.url_token = reverse('token_obtain')
        cls.url_refresh = reverse('token_refresh')
        cls.credentials = {
                "email": "user@user.com",
                "password": "Nepal@123"
                }
        cls.client = APIClient()

    def test_session_authentication(self):
        is_loggedin = self.client.login(email="user@user.com", password="Nepal@123")
        self.assertEqual(is_loggedin, True)

    def test_jwt_token_receive(self):
        resp = self.client.post(self.url_token, self.credentials, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.status_text, 'OK')

    def test_jwt_token_authentication(self):
        resp = self.client.post(self.url_token, self.credentials, format='json')
        access_token = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        resp = self.client.get(reverse('me'), data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK, resp.content)
