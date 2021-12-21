from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel

# Create your views here.


class ProductListView(ListView):
    template_name = "shop.html"
    queryset = ProductModel.objects.order_by('-pk')

