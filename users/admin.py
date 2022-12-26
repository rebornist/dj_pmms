from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# # Register your models here.
# @admin.register(models.User)
# # class CustomUserAdmin(admin.ModelAdmin):
# class CustomUserAdmin(UserAdmin):
    
#     """ 
#     Custom User Admin 
    
#     list_display = ('username', 'email', 'gender', 'language', 'superuser')
#     list_filter = ('superuser', 'gender')
#     """
    
#     fieldsets = UserAdmin.fieldsets + (
#         (
#             "Custom Profile", 
#             {
#                 "fields": (
#                     "avatar"
#                 )
#             },
#         ),
#     )
    
#     list_filter = UserAdmin.list_filter

#     list_display = (
#         "username",
#         "first_name",
#         "last_name",
#         "email",
#         "is_active",
    #     "is_staff",
    #     "is_superuser",
    # )
    

