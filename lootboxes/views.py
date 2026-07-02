from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to return all products page"""

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'lootboxes/loot.html', context)



def product_detail(request, product_id):
    """ A view to return the detail page for a specific product"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'lootboxes/loot_detail.html', context)