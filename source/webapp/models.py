from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True, upload_to='product_pics')
    brand = models.ForeignKey('webapp.Brand', on_delete=models.SET_DEFAULT, default='Не указано', related_name='products')
    category = models.ForeignKey('webapp.Category', on_delete=models.PROTECT, related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)


class Brand(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    logo = models.ImageField(verbose_name='логотип',upload_to='product_pics')


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
