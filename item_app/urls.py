from django.urls import path
from .views import All_items, An_item, Item_by_category

urlpatterns = [
    path('', All_items.as_view(), name='all_items'),
    path('<int:item_id>/', An_item.as_view(), name='an_item'),
    path('category/<str:category>/', Item_by_category.as_view(), name="items_by_category"),
]
