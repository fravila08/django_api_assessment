from django.db import models

# Create your models here.
class Item(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)