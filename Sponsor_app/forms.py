from django import forms
from .models import ActiveSponsor

class ActiveSponsorForm(forms.ModelForm):
    class Meta:
        model = ActiveSponsor
        fields = ['BrandName', 'BrandType', 'SponsorPhone', 'SponsorEmail']
