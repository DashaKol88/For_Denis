from django.contrib import admin
from .models import Author, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at',)
    list_filter = ('author', 'created_at',)
