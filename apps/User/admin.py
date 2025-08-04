from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from apps.Authentication.signals import *

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Location

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ('customer_number', 'is_active', 'is_staff', 'is_superuser', 'email', 'company_name','phone', )
    
    fieldsets = (
        (None, {'fields': ('customer_number','company_name', 'name', 'email', 'phone', 'address', 'password')}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',              # ✅ group permission
                'user_permissions',    # ✅ individual permission
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'customer_number','company_name','name', 'email', 'phone', 'address',
                'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser',
                'groups',              # ✅ group permission
                'user_permissions',    # ✅ individual permission
            )}
        ),
    )

    search_fields = ('customer_number','company_name', 'email', 'phone')
    ordering = ('customer_number',)

admin.site.register(CustomUser, CustomUserAdmin)




# from django.contrib.auth.admin import UserAdmin
# from django.contrib import admin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('customer_number', 'is_active', 'is_staff', 'is_superuser', 'email', 'phone', 'address')
#     fieldsets = (
#         (None, {'fields': ('customer_number', 'email', 'phone', 'address')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Password', {
#             'fields': ('password',),
#             'description': "Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"../password/\">this form</a>."
#         }),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('customer_number', 'email', 'phone', 'address', 'password1', 'password2', 'is_active', 'is_staff')}
#         ),
#     )
#     search_fields = ('customer_number', 'email', 'phone')
#     ordering = ('customer_number',)
#     readonly_fields = ('password',)

#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('<id>/password/', self.admin_site.admin_view(self.user_change_password), name='auth_user_password_change'),
#         ]
#         return custom_urls + urls

# admin.site.register(CustomUser, CustomUserAdmin)