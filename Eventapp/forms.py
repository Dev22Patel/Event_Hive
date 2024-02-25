# eventApp/forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    # Optional: Add custom field validation or widgets here
    # Example of custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Please use an email ending with @example.com")
        return email

    # Example of custom widget for date fields
    event_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    bidding_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = [
            'organizer_name', 
            'organizer_phone', 
            'event_date', 
            'email', 
            'sponsor_types', 
            'bidding_date', 
            'description', 
        ]
        # Example of how to customize widgets for all fields in Meta
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'sponsor_types': forms.CheckboxSelectMultiple(),  # Assuming it's a ManyToManyField or similar
            # Any other custom widgets for specific fields can be defined here
        }
