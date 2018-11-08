from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name = 'list_view'),
    path('<category_slug>/', list_view, name = 'category_list_view'),
    path('<category_slug>/<slug>', detail_view, name = 'detail_view'),
]