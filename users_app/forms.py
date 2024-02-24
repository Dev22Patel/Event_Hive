from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_email_unique(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError("Email already exists.")

class CustomRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True, validators=[validate_email_unique])
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', "Password must match.")

        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        return user
