from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product
from catalog.forms import ContactForm

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm()

    return render (request, 'contact.html', {"form": form})


