from datetime import datetime

import pytz as pytz
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# Product


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categorys')


class BrandModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ProductTagModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class SizeModel(models.Model):
    title = models.CharField(max_length=3, verbose_name=_("title"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ColorModel(models.Model):
    code = models.CharField(max_length=20, verbose_name=_("code"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to="products", verbose_name=_('image'))
    price = models.FloatField(max_length=100, verbose_name=_('price'))
    real_price = models.IntegerField(default=0, verbose_name=_('real price'))
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name="products", verbose_name=_('brand'))
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name="products",
                                 verbose_name=_('category'))
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)], # skidka 100 ta oshib ketmasin
        verbose_name=_('discount'))

    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    sizes = models.ManyToManyField(SizeModel, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products',
                                  verbose_name=_('tags'))  # default null many to may ozi qaytaradi
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0  # agar no'lga teng bo'lmasa true qaysin

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    def get_related_products(self):
        return self.category.products.exclude(pk=self.pk)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('product'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def str(self):
        return self.product.title

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')