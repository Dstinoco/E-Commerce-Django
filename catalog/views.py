from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,

    }

    return render(request, 'catalog/category.html', context)



def product_list(request):
    products = Product.objects.all() 

    return render(request, 'catalog/product_list.html',{"products": products} )



def produtos_unitario(request, produto_slug):
    produto_unitario = Product.objects.get(slug=produto_slug)
    return render(request, 'catalog/product.html', {"produto_unitario": produto_unitario} )
