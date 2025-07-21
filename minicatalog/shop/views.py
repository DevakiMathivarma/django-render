from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import user_passes_test

def product_list(request):
    products = Product.objects.filter(stock__gt=0)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': p})
