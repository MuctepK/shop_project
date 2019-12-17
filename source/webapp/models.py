from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    brand = models.ForeignKey('webapp.Brand', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    category = models.ForeignKey('webapp.Category', on_delete=models.PROTECT, related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    description = RichTextUploadingField('content')
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', upload_to='product_pics')


class Brand(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    logo = models.ImageField(verbose_name='логотип',upload_to='product_pics', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    image = models.ImageField('Картинка категории', upload_to='categories_pics', null=True)

    def __str__(self):
        return self.name