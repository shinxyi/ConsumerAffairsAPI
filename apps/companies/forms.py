from django import forms
from .models import Company
from django.core.exceptions import ValidationError

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model=Company
        exclude = ['active', 'created_at', 'updated_at', 'created_by']
