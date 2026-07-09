from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportTicketForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def crawler_support(request):
    """
    Unified Support Terminal: Handles displaying the form with pre-populated
    user data, saving tickets to the database,
    and dispatching confirmation emails.
    """
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)

            if request.user.is_authenticated:
                ticket.user = request.user

            ticket.save()

            ticket.refresh_from_db()
            ticket_id = ticket.ticket_id_string if ticket.ticket_id_string else "CONFIRMED"   # noqa: E501

            user_email = form.cleaned_data['email']
            user_name = form.cleaned_data['full_name']
            severity_label = dict(ticket.SEVERITY_CHOICES).get(ticket.severity, ticket.severity)   # noqa: E501

            subject = f"[Crawler Emporium] Support Ticket Logged - {ticket_id}"
            body_message = (
                f"Hello {user_name},\n\n"
                f"This transmission confirms that your support ticket ({ticket_id}) has been successfully received by our automated systems.\n\n"   # noqa: E501
                f"--- Your Ticket Summary ---\n"
                f"Subject: {form.cleaned_data['subject']}\n"
                f"Severity Matrix: {severity_label}\n"
                f"Message Log:\n{form.cleaned_data['message']}\n"
                f"---------------------------\n\n"
                f"Our support desk will review your complaint details and follow up with a response...... probably.\n\n"   # noqa: E501
                f"Thank you for your patience,\n"
                f"Crawler Emporium Support Desk"
            )

            try:
                send_mail(
                    subject,
                    body_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email Dispatch Failure: {e}")

            messages.success(
                request,
                f"Ticket logged under token: {ticket_id}. A confirmation has been sent via email. "   # noqa: E501
                f"Don't hold your breath waiting for a reply crawler."
            )

            return redirect('crawler_support')

    else:
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
