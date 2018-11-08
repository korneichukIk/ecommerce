from django.urls import path
from .views import list_view, detail_view, cart_detail, add_to_cart, remove_from_cart

urlpatterns = [
    path('', list_view, name = 'list_view'),
    path('cart/', cart_detail, name = 'cart'),
    path('add_to_cart/<product_id>', add_to_cart, name = 'add'),
    path('remove_from_cart/<product_id>', remove_from_cart, name = 'remove'),
    path('<category_slug>/', list_view, name = 'category_list_view'),
    path('<category_slug>/<slug>', detail_view, name = 'detail_view'),
]