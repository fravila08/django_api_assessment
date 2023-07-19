from django.test import TestCase, Client
from django.urls import reverse



"""
This test will send a post request to the 'signup' endpoint with a request body of
{"email":"fr@fr.com", "password":"fr"} to simulate a user sending a post request to signup. 

This endpoint must return the following Response

{"client":"fr@fr.com","token":"<token_generated>"} with a status code of 201 
in order to pass this test
"""


class Test_user_sign_up(TestCase):
    def test_001_user_sign_up(self):
        client = Client()
        response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        # print(response.content)
        with self.subTest():
            self.assertEquals(response.status_code, 201)
        self.assert_(
            b'{"client":"fr@fr.com"' in response.content
            and b"token" in response.content
        )
