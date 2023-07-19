from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Cart_item, Cart
from .serializers import CartItemSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.response import Response
# Create your views here.

class Cart_manager(APIView):
    def get(self, request):
        cart = get_object_or_404(Cart, client = request.user)
        cart_items = Cart_item.objects.filter(cart = cart)
        items = CartItemSerializer(cart_items, many=True)
        price = sum([x.item.price * x.quantity for x in cart_items])
        return Response({"cart_items":items.data, "total_price":price})
    
    def put(self, request, method, cart_item_id):
        cart_item = get_object_or_404(Cart_item, id = cart_item_id)
        if method == 'add':
            cart_item.quantity +=1
            cart_item.save()
        elif method == 'sub':
            cart_item.quantity -= 1
            cart_item.save()
            if cart_item.quantity == 0:
                cart_item.delete()
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_204_NO_CONTENT)
    
    def delete(self, request, cart_item_id):
        cart_item = get_object_or_404(Cart_item, id = cart_item_id)
        cart_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)

