from django.urls import path
from .views import *

app_name='product'
urlpatterns = [
    path('latest-products/',LatestProductsList.as_view(),name='latestproducts'),
    path('products/<slug:category_slug>/<slug:product_slug>/',ProductDetail.as_view(),name='productdetail'),
    path('products/<slug:category_slug>/',CategoryDetail.as_view(),name='categorydetail'),
    path('products_djackets/search/',searchProduct,name='searchProduct')
]
