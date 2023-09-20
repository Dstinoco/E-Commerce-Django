
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact
from catalog import views as views_catalog



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contato/', contact, name='contato'),
    path('', include('catalog.urls', namespace="catalog-")),
]
