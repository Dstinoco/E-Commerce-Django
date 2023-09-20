from django.urls import path
from catalog.views import product_list, category, produtos_unitario

app_name = "catalog"
urlpatterns = [
    path('produtos/', product_list, name='product_list'),
    path('produtos/categoria/<str:category_name>', category, name='category'),
    path('produtos/<int:produto_id>', produtos_unitario, name='produtos_unitario'),
    ]