
from django.contrib import admin
from django.urls import path
from core.views import index, product, product_list, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('produto/', product),
    path('lista_produto/', product_list),
    path('contato/', contact),
]
