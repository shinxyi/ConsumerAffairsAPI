from django.contrib import admin
from .models import Company as Companies

# Register your models here.
class CompaniesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Companies,CompaniesAdmin)
