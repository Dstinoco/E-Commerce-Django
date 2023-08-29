from django.contrib import admin
from catalog.models import Category, Product

class ListandoCategory(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    



class ListandoProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    
    



admin.site.register(Category, ListandoCategory)
admin.site.register(Product, ListandoProduct)