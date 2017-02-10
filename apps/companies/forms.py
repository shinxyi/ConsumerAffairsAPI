from django import forms
from .models import Company
from django.core.exceptions import ValidationError

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model=Company
        fields = '__all__'
