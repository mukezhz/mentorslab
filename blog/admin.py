from django.contrib import admin
from .models import Blog, BlogComment


@admin.register(Blog)
class ForumModelAdmin(admin.ModelAdmin):
    list_display = [
            'topic',
            'author',
            'created_date'
            ]


@admin.register(BlogComment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'blog',
            'created_date',
            ]
