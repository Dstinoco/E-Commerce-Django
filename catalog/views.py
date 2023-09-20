from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,

    }

    return render(request, 'catalog/category.html', context)



def product_list(request):
    products = Product.objects.all() 

    return render(request, 'catalog/product_list.html',{"products": products} )



def produtos_unitario(request, produto_id):
    produto = get_object_or_404(Product, pk=produto_id)
    return render(request, 'catalog/product.html', {"produto": produto} )
