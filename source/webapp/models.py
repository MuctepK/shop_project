from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from datetime import date

class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    brand = models.ForeignKey('webapp.Brand', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    category = models.ForeignKey('webapp.Category', on_delete=models.PROTECT, related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    description = RichTextUploadingField('content')
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    old_price = models.IntegerField(verbose_name='Старая цена', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления', null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def get_discount(self):
        return round((self.old_price-self.price)/((self.price+self.old_price)/2)*100)

    def main_image(self):
        return self.images.all().first().image

    def get_images(self):
        return [item.image.url for item in self.images.all()]

    def is_new(self):
        return (date.today() - date(self.created_at)).days <= 7

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


class Review(models.Model):
    author = models.CharField(max_length=128, verbose_name='Автор')
    text = models.TextField(max_length=512, verbose_name='Текст')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    mark = models.IntegerField(verbose_name='Оценка')
    verified = models.BooleanField(verbose_name='Подтверждено', default=False)
