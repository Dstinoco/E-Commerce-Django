from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product
from catalog.forms import ContactForm
from django.views.generic import *


class indexView(TemplateView):
    template_name = 'index.html'


def contact(request):
    form = ContactForm()

    return render (request, 'contact.html', {"form": form})


index = indexView.as_view()