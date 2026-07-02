from django.conf import settings

def backpack_contents(request):

    backpack_items = []
    total = 0
    product_count = 0


    context = {
        'backpack_items': backpack_items,
        'total': total,
        'product_count': product_count,
    }

    return context