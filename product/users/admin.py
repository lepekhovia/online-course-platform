from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from courses.models import Course, Lesson, Group, Balance, Purchase


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Админка для кастомной модели пользователя"""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'), }),)

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('email',)


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(Balance)
admin.site.register(Purchase)
