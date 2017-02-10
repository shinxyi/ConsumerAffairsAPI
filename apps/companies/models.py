from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from ..loginreg.models import User
import re

# Create your models here.

def validateUrl(value):
    pattern = re.compile(r'^((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)+$')

    if not pattern.match(value):
        raise ValidationError(
          '{} is not a proper url'.format(value)
          )

class Company(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=False)
    location = models.CharField(max_length=100, blank=False)
    industry = models.CharField(max_length=45, blank=False)
    current_status = models.CharField(max_length=20, blank=False)
    website = models.CharField(max_length=100, validators = [validateUrl])
    service_description=models.TextField(max_length=10000, blank=False)
    created_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
