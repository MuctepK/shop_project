# Generated by Django 2.2.5 on 2019-12-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
    ]
