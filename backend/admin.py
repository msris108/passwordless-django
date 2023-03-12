from django.contrib import admin
from .models import CustomUser

# Register models here for admin page

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass