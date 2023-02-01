from django.shortcuts import render

from .models import Product


def home(request):
    """View displaying the homepage of the website."""
    products = Product.objects.all()
    return render(
        request,
        "exemple/home.html",
        {
            "products": products,
        },
    )


def detail(request):
    """View displaying the product details."""
    products = Product.objects.all()
    return render(
        request,
        "exemple/home.html",
        {
            "products": products,
        },
    )
