from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json
from rest_framework.authtoken.models import Token



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user and delete this users Token. Then the user will sent a POST request
to logout to force the deletion of their Token.

This endpoint must return the following Response status code of 204 
in order to pass this test
"""


class Test_user_logout(APITestCase):
    def test_004_user_logout(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.post(reverse("logout"))
        with self.subTest():
            tokens = Token.objects.all()
            self.assertEquals(len(tokens), 0)
        self.assertEquals(response.status_code, 204)