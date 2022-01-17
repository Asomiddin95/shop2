from django.contrib import admin
from product.models import CategoryModel, BrandModel, ProductTagModel, ProductModel, SizeModel, ColorModel, \
    ProductImageModel
from .forms import ColorModelForm
from modeltranslation.admin import TranslationAdmin
#
#
# # Register your models here.


class MyProductAdminTrans(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyProductAdminTrans):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


#
@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


# #
@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title ']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['code']
    form = ColorModelForm


class ProductImageStack(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(MyProductAdminTrans):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand', 'colors', 'sizes']
    readonly_fields = ['real_price']
    inlines = [ProductImageStack]


