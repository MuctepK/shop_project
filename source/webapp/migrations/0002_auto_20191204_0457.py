# Generated by Django 2.2.5 on 2019-12-04 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [

        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='product_pics', verbose_name='логотип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='webapp.Brand'),
        ),
    ]
