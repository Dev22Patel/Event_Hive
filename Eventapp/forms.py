from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'LeadOrganizerName', 
            'LeadOrganizerPhone', 
            'EventDate', 
            'LeadOrganizerEmail', 
            # 'SponsorTypes', 
            'BiddingDate', 
            'Description', 
        ]
        widgets = {
            'EventDate': forms.DateInput(attrs={'type': 'date'}),
            'BiddingDate': forms.DateInput(attrs={'type': 'date'}),
            'Description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            # Since 'SponsorTypes' is a JSONField, consider how you want to present this in the form.
            # You might need a custom widget or method to handle the input and conversion to JSON.
        }

    def clean_LeadOrganizerEmail(self):
        email = self.cleaned_data.get('LeadOrganizerEmail')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Please use an email ending with @gmail.com")
        return email
