
from django.contrib import admin
from django.urls import path, include
from core.views import index, product, product_list, contact
from catalog import views as views_catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('produto/', product, name='produto'),
    path('contato/', contact, name='contato'),
    path('produtos/', include('catalog.urls', namespace="catalog-")),
]
