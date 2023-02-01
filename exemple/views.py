from django.shortcuts import render, get_object_or_404

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


def detail(request, slug):
    """View displaying the product details."""
    product = get_object_or_404(Product, kwargs={"slug": slug})
    return render(
        request,
        "exemple/home.html",
        {
            "products": product,
        },
    )
