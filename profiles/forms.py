from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Comms Contact Number',
            'default_postcode': 'Postal Transit Code',
            'default_town_or_city': 'City',
            'default_street_address1': 'Street Address Line 1',
            'default_street_address2': 'Street Address Line 2',
            'default_county': 'County / Region',
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
                self.fields[field].label = placeholders[field]
            
            self.fields[field].widget.attrs['class'] = 'form-control bg-dark border-secondary text-light custom-search-input py-2'