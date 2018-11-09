from django.urls import path
from .views import order_create, order_pdf

urlpatterns = [
    path('admin/order/<order_id>/pdf/', order_pdf, name = 'order_pdf'),
    path('create/', order_create, name = 'order_create'),
]