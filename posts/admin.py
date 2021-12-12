from django.contrib import admin
from .models import PostModel, AuthorModel, TagModel


# Register your models here.
@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


#
@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author','tags']  # 2 ulangan polya  korinish o'zgaradi
