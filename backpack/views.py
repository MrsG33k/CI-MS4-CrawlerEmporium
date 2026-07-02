from django.shortcuts import render

# Create your views here.

def view_backpack(request):
    """ A view to return the backpack page"""
    return render(request, 'backpack/backpack.html')
