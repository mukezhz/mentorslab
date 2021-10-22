from django.contrib import admin
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'uuid']


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','title', 'uuid', 'id', 'tags', 'languages',]
