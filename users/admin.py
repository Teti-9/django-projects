from django.contrib import admin
from .models import CustomUserModel

@admin.register(CustomUserModel)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'password')
    
    ordering = ('username', 'email', 'password')

    exclude = ('last_login', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'groups', 'user_permissions')