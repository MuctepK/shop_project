from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'the_slug'
    context_object_name = 'product'



