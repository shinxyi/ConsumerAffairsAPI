from django import forms
from .models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        exclude = ['active', 'auth_token']
        widgets = {
            'password': forms.PasswordInput,
            'confirm_password': forms.PasswordInput
        }
