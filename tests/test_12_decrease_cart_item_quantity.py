from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user and delete this users Token.

The client will send a mix of POST and DELETE request to the endpoint with the name of "an_item" to build
the clients cart. 

The client will then send two PUT requests to the endpoint with the name of "cart_item_quantity"
and pass in "add" as the method and the number 15 as the cart_item_id to increment the quantity 
of the Cart_item with the ID of 15 to 3.

The client will then send a third and final PUT request to the endpoint with the name of "cart_item_quantity"
and pass in "sub" as the method and the number 15 as the cart_item_id to decrement the quantity 
of the Cart_item with the ID of 15 to 2. 

The client will send a GET request to the endpoint with the name of "cart" to see their updated cart items 
and price.
This endpoint must return the following Response status code of 200
"""
answer = {
    "cart_items": [
        {
            "id": 13,
            "item": {
                "id": 10,
                "category": "Other",
                "name": "Wireless Keyboard and Mouse",
                "price": "20.03",
            },
            "quantity": 1,
        },
        {
            "id": 14,
            "item": {
                "id": 9,
                "category": "Other",
                "name": "Code Editor Subscription",
                "price": "50.10",
            },
            "quantity": 1,
        },
        {
            "id": 15,
            "item": {
                "id": 3,
                "category": "Electronics",
                "name": "Lenovo ThinkPad",
                "price": "200.30",
            },
            "quantity": 2,
        },
        {
            "id": 16,
            "item": {
                "id": 5,
                "category": "Books",
                "name": "Cracking the Coding Interview",
                "price": "30.27",
            },
            "quantity": 1,
        },
    ],
    "total_price": 501.0,
}
"""
in order to pass the test. Pay attention to order and formatting of your data.
"""


class Test_decrease_cart_item(APITestCase):
    fixtures = ["items.json"]

    def test_012_decrease_cart_item(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        self.client.post(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[9]))
        self.client.post(reverse("an_item", args=[3]))
        self.client.post(reverse("an_item", args=[5]))
        self.client.put(reverse("cart_item_quantity", args=['add', 15]))
        self.client.put(reverse("cart_item_quantity", args=['add', 15]))
        self.client.put(reverse("cart_item_quantity", args=['sub', 15]))
        response = self.client.get(reverse("cart"))
        # print(response.content)
        with self.subTest():
            self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), answer)
