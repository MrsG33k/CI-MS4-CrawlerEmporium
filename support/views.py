from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportTicketForm

# Create your views here.

def crawler_support(request):
    """ Support Terminal with details of logged in users populated """
    
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            
            # Check if the user is authenticated
            if request.user.is_authenticated:
                ticket.user = request.user
                
            # Append the TICK# to the ticket number
            ticket.save()
            
            messages.success(
                request, 
                f"Ticket logged under token: {ticket.ticket_id_string}. Don't hold your breath waiting for a reply crawler."
            )
            return redirect('crawler_support')
    else:
        # GET Request
        initial_data = {}
        
        if request.user.is_authenticated:
            user = request.user
            full_name = f"{user.first_name} {user.last_name}".strip()
            
            initial_data = {
                'full_name': full_name if full_name else user.username,
                'email': user.email
            }
            
        form = SupportTicketForm(initial=initial_data)
        
    context = {
        'form': form,
    }
    
    return render(request, 'support/support.html', context)