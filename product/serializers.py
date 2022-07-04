from rest_framework import serializers
from .models import *

#!ProductSerializers
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id','name','description','price',
            'get_absolute_url','get_image','get_thumbnail'
        ]

#!CategorySerializers
class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)
    
    class Meta:
        model = Category
        fields = ['id','name','get_absolute_url','products']