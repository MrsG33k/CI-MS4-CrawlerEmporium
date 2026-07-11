from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to return all products page"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")   # noqa: E501
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(sample_contents__icontains=query) | Q(rarity__icontains=query)   # noqa: E501
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'lootboxes/loot.html', context)


def product_detail(request, product_id):
    """ A view to return the detail page for a specific product"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'lootboxes/loot_detail.html', context)


@login_required
def add_product(request):
    """ Add a new lootbox to the store  """
    if not request.user.is_superuser:
        messages.error(request, 'ERROR: Unauthorised crawler. Access restricted to AI Admins.')   # noqa:E501
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'SUCCESS: Logged new Lootbox: {product.name}!')   # noqa:E501
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'ERROR: Data validation failure. Please check form fields.')   # noqa:E501
    else:
        form = ProductForm()

    template = 'lootboxes/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing lootbox to the store """
    if not request.user.is_superuser:
        messages.error(request, 'ERROR: Unauthorised crawler. Access restricted to AI Admins.')   # noqa:E501
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'SUCCESS: Updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'ERROR: Data validation failure. Please check form fields.')   # noqa:E501
    else:
        form = ProductForm(instance=product)

    template = 'lootboxes/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a lootbox from the system entirely """
    if not request.user.is_superuser:
        messages.error(request, 'ERROR: Unauthorised crawler. Access restricted to AI Admins.')   # noqa:E501
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'SUCCESS: {product.name} has been jettisoned from the database.')   # noqa:E501
    return redirect(reverse('products'))
