from django.contrib import admin
from .models import Review as Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reviews,ReviewsAdmin)
