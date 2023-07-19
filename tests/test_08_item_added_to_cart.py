from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user and delete this users Token.

This endpoint must return the following Response status code of 201
"""

answer = "Wireless Keyboard and Mouse has been added to your cart"

"""
In order to pass the test. Pay attention to order and formatting of your data.
"""

class Test_added_to_cart(APITestCase):
    fixtures=["items.json"]

    def test_008_added_to_cart(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.post(reverse("an_item", args=[10]))
        with self.subTest():
            self.assertEquals(response.status_code, 201)
        self.assertEquals(json.loads(response.content), answer)