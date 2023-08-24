
from django.contrib import admin
from django.urls import path
from core.views import index, product, product_list, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('produto/', product, name='produto'),
    path('lista_produto/', product_list, name='lista_produto'),
    path('contato/', contact, name='contato'),
]
