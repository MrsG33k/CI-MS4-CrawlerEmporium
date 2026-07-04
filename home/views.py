from django.shortcuts import render
from lootboxes.models import Product

def index(request):
    """ A view to return the index page with dynamic loot boxes """
    
    # Fetch all the loot
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, 'home/index.html', context)