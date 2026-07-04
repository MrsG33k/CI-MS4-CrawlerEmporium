from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import Orderform

# Create your views here.

def  checkout(request):
    backpack = request.session.get('backpack', {})
    if not backpack:
        messages.error(request, "There's nothing in your backpack at the moment")
        return redirect(reverse('lootboxes'))
    
    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
