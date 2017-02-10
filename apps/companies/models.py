from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from ..loginreg.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=False)
    location = models.CharField(max_length=100, blank=False)
    industry = models.CharField(max_length=45, blank=False)
    current_status = models.CharField(max_length=20, blank=False)
    website = models.CharField(max_length=100, blank=True)
    service_description=models.TextField(max_length=10000, blank=False)
    created_by = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
