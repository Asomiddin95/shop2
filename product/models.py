from datetime import datetime

import pytz as pytz
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# Product

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'


class BrandModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductTagModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products")
    price = models.FloatField(max_length=100)
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name="products")
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])  # skidka 100 ta oshib ketmasin

    short_description = models.TextField()
    long_description = RichTextUploadingField()
    tags = models.ManyToManyField(ProductTagModel, related_name='products')  # default null many to may ozi qaytaradi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0  # agar no'lga teng bo'lmasa true qaysin

    def get_price(self):
        if self.is_discount(): # agar tavar-skidkaga bolsa
            return self.price - self.price * self.discount / 100
        return self.price

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
