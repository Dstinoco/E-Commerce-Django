from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView


class ProductListView(ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3
    

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,

    }

    return render(request, 'catalog/category.html', context)


def produtos_unitario(request, produto_slug):
    produto_unitario = Product.objects.get(slug=produto_slug)
    return render(request, 'catalog/product.html', {"produto_unitario": produto_unitario} )



product_list = ProductListView.as_view()    
