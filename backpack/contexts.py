from django.conf import settings
from django.shortcuts import get_object_or_404
from lootboxes.models import Product

def backpack_contents(request):

    backpack_items = []
    total = 0
    product_count = 0
    backpack = request.session.get('backpack', {})

    for item_id, quantity in backpack.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        backpack_items.append({
            'item_id': item_id,
            'quantity':quantity,
            'product':product,
        })


    context = {
        'backpack_items': backpack_items,
        'total': total,
        'product_count': product_count,
    }

    return context