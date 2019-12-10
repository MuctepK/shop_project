from django.contrib import admin
from webapp.models import Product, Category, Brand

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)

