from modeltranslation.translator import register, TranslationOptions
from .models import PostModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

