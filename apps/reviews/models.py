from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from ..loginreg.models import User
from ..companies.models import Company
# Create your models here.
def validateRating(value):
    if value<1 or value>5:
        raise ValidationError(
          'Rating must between 1-5.'
          )

class Review(models.Model):
    title = models.CharField(max_length=64, blank=False)
    rating = models.PositiveIntegerField(blank=False, validators= [validateRating])
    summary = models.TextField(max_length=10000, blank=False)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
