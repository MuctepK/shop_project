from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe

from webapp.models import Product, Category, Brand, Image
from django.utils.html import format_html

from django.contrib.admin.widgets import AdminFileWidget


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % (image_url, image_url, file_name, ''))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageAdmin(admin.TabularInline):
    extra = 3
    model = Image
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]


admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)