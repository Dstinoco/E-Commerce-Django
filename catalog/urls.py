from django.urls import path
from catalog.views import product_list, category

app_name = "catalog"
urlpatterns = [
    path('', product_list, name='product_list'),
    path('categoria/<str:category_name>/', category, name='category'),
    ]