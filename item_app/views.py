from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from cart_app.models import Cart_item, Cart
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

# Create your views here.
class All_items(APIView):
    def get(self, request):
        items = ItemSerializer(Item.objects.all(), many = True)
        return Response(items.data)

class An_item(APIView):
    def get(self, request, item_id):
        item = ItemSerializer(get_object_or_404(Item, id = item_id))
        return Response(item.data)
    
    def post(self, request, item_id):
        item = get_object_or_404(Item, id = item_id)
        cart = Cart.objects.get(client = request.user)
        cart_item = Cart_item.objects.create(item = item, cart = cart)
        cart_item.save()
        return Response(f"{item.name} has been added to your cart", status=HTTP_201_CREATED)

    def delete(self, request, item_id):
        item = get_object_or_404(Item, id = item_id)
        cart_item = get_object_or_404(Cart_item, item = item)
        cart_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Item_by_category(APIView):
    def get(self, request, category):
        items = ItemSerializer(Item.objects.filter(category = category.title()), many = True)
        return Response(items.data)