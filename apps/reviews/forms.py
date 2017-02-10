from django import forms
from .models import Review
from django.core.exceptions import ValidationError

class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = ['title', 'rating', 'summary']
