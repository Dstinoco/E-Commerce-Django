from django.urls import path

from catalog.views import product_list, category, produtos_unitario


urlpatterns = [
    path('produtos/', product_list, name='product_list'),
    path('produtos/categoria/<slug:category_slug>/', category, name='category'),
    path('produtos/categoria/<slug:produto_slug>', produtos_unitario, name='produto_unitario'),
    ]