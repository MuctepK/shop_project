from django.urls import path

from webapp.views import ProductListView, ProductDetailView

app_name = 'webapp'
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<slug:the_slug>', ProductDetailView.as_view(), name='product_detail')
]