from django.contrib import admin
from user.models import User, Post


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_at', 'updated_at', 'user']
