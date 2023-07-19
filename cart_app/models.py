from django.db import models
from user_app.models import Client
from item_app.models import Item

# Create your models here.
class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
