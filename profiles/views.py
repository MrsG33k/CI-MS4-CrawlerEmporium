from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile_vault(request):
    """ Display the crawler's historic transaction ledger only. """
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile_vault.html'
    context = {
        'orders': orders,
    }
    return render(request, template, context)

@login_required
def account_settings(request):
    """ Display and update the user's identity details and shipping matrix. """
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Secure coordinates and profile updated.')
        else:
            messages.error(request, 'Update failed. Check system parameters.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/account_settings.html'
    context = {
        'form': form,
    }
    return render(request, template, context)