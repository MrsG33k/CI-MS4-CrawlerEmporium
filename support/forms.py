from django import forms
from .models import SupportTicket


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket

        fields = ['full_name', 'email', 'subject', 'severity', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Identify yourself, meat sack. (Crawler Name)...',
            'email': 'Email address for corporate'
            'spam and generic condolences...',
            'subject': 'Which part of my flawlessly designed'
            'system are you blaming your incompetence on?',
            'message': 'Cry about your discrepancies here.'
            'Be descriptive, I love reading about your struggles...'
        }

        for field_name, placeholder in placeholders.items():
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': placeholder
            })

        self.fields['severity'].widget.attrs.update({
            'class': 'form-select bg-dark text-white border-secondary'
        })
