from django.contrib import admin
from django.contrib.admin.sites import site

from .models import User, Todo

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator']


site.register(Todo, TodoAdmin)
site.register(User, UserAdmin)
