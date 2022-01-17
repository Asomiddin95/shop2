from modeltranslation.translator import register, TranslationOptions
from product.models import CategoryModel, ProductModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('short_description', 'long_description')
