from django.contrib import admin
from .models import PostModel, AuthorModel, TagModel, CommentModel
from modeltranslation.admin import TranslationAdmin


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
class PostAdmin(TranslationAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']  # 2 ulangan polya  korinish o'zgaradi

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
