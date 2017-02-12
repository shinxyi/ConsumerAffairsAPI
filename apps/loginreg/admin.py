from django.contrib import admin
from .models import User as Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Users,UsersAdmin)
