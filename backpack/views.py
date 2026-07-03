from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from lootboxes.models import Product

# Create your views here.

def view_backpack(request):
    """ A view to return the backpack page"""
    return render(request, 'backpack/backpack.html')

def add_to_backpack(request, item_id):
    """Add an item to the backpack (cart)"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    backpack = request.session.get('backpack',{})

    if item_id in list(backpack.keys()):
        backpack[item_id] += quantity
    else:
        backpack[item_id] = quantity
    
    request.session['backpack'] = backpack
    messages.success(request, f"INVENTORY EXPANSION: You added '{product.name}' to your secure backpack!")
    return redirect(redirect_url)

# Update backpack and remove from backpack created in collaboration with Michael Whittaker

def update_backpack(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        backpack[item_id] = quantity
    else:
        backpack.pop(item_id, None)

    request.session['backpack'] = backpack
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return HttpResponse(status=200)
        
    return redirect(reverse('view_backpack'))

def remove_from_backpack(request, item_id):
    """Remove the item from the shopping backpack session storage"""
    try:
        backpack = request.session.get('backpack', {})
        
        if item_id in backpack:
            backpack.pop(item_id)
            
        request.session['backpack'] = backpack

        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)
    

