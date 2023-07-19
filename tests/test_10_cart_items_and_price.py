from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user and delete this users Token.

This endpoint must return the following Response status code of 200
"""
answer = {
    "cart_items": [
        {
            "id": 4,
            "item": {
                "id": 10,
                "category": "Other",
                "name": "Wireless Keyboard and Mouse",
                "price": "20.03",
            },
            "quantity": 1,
        },
        {
            "id": 5,
            "item": {
                "id": 9,
                "category": "Other",
                "name": "Code Editor Subscription",
                "price": "50.10",
            },
            "quantity": 1,
        },
        {
            "id": 6,
            "item": {
                "id": 3,
                "category": "Electronics",
                "name": "Lenovo ThinkPad",
                "price": "200.30",
            },
            "quantity": 1,
        },
        {
            "id": 7,
            "item": {
                "id": 5,
                "category": "Books",
                "name": "Cracking the Coding Interview",
                "price": "30.27",
            },
            "quantity": 1,
        },
    ],
    "total_price": 300.7,
}
"""
in order to pass the test. Pay attention to order and formatting of your data.
"""


class Test_cart_items_and_total_price(APITestCase):
    fixtures = ["items.json"]

    def test_010_cart_items_and_total_price(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        self.client.post(reverse("an_item", args=[10]))
        self.client.delete(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[9]))
        self.client.post(reverse("an_item", args=[3]))
        self.client.post(reverse("an_item", args=[5]))
        response = self.client.get(reverse("cart"))
        with self.subTest():
            self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), answer)
