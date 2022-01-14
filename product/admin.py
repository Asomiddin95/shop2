from django.contrib import admin
from product.models import CategoryModel, BrandModel, ProductTagModel, ProductModel, SizeModel, ColorModel
from .forms import ColorModelForm

#
#
# # Register your models here.
#


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
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
    list_display = ['size', 'created_at']
    list_filter = ['created_at']
    search_fields = ['size']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['code']
    form = ColorModelForm


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand', 'color', 'size']
