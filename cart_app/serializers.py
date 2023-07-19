from rest_framework import serializers
from item_app.serializers import ItemSerializer
from .models import Cart_item

class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Cart_item
        fields = ['id','item', 'quantity']