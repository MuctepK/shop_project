# Generated by Django 2.2.5 on 2019-12-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Старая цена'),
        ),
    ]
