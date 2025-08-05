from modeltranslation.translator import register , TranslationOptions
from products.models import Products


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('name','quantity')