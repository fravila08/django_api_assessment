from django.urls import path
from .views import Cart_manager

urlpatterns = [
    path("", Cart_manager.as_view(), name="cart"),
    path(
        "method/<str:method>/cart_item/<int:cart_item_id>/",
        Cart_manager.as_view(),
        name="cart_item_quantity",
    ),
    path("<int:cart_item_id>/", Cart_manager.as_view(), name="delete_item")
]
