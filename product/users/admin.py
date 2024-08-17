from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Админка для кастомной модели пользователя"""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'), }),)

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('email',)
