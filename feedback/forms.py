from django import forms
from .models import Review

class reviewform(forms.ModelForm):  # Corrected class name to UserImageForm
    class Meta:  # Corrected capitalization to Meta
        model = Review  # Corrected attribute name to model
        fields = '__all__'