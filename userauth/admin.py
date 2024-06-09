from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User_register, UserInfo

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'user_type', 'is_admin')
    list_filter = ('is_admin', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('user_type',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User_register, UserAdmin)
admin.site.register(UserInfo)
