from django.urls import path
from .views import *

app_name='order'
urlpatterns = [
    path('checkout/',checkOut,name='checkOut'),
    path('orders/',OrderList.as_view(),name='orders')
]
