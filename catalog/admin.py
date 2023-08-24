from django.contrib import admin
from catalog.models import Category, Product

class ListandoCategory(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')



class ListandoProduct(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    



admin.site.register(Category, ListandoCategory)
admin.site.register(Product, ListandoProduct)