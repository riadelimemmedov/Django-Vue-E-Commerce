from django.shortcuts import render,Http404
from django.db.models import Q

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
#!LatestProductsList
class LatestProductsList(APIView):
    def get(self,request,format=None):#if this view GET request work this function
        products = Product.objects.all()[0:4]
        serializers = ProductSerializers(products,many=True)
        return Response(serializers.data)

#!ProductDetail
class ProductDetail(APIView):
    def get_object(self,category_slug,product_slug):
        print('get_object isledi')
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self,request,category_slug,product_slug,format=None):
            print('get isledi')
            product = self.get_object(category_slug,product_slug)
            serializer = ProductSerializers(product)
            return Response(serializer.data)

#!CategoryDetail
class CategoryDetail(APIView):
    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self,request,category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializers(category)
        return Response(serializer.data)

#!searchProduct
@api_view(['POST'])
def searchProduct(request):
    print('Successfully worked search produc view')
    product_name = request.data.get('product_name','')#get request data this way => request.data.get('input_name')
    
    if product_name:
        products = Product.objects.filter(Q(name__icontains=product_name)|Q(description__icontains=product_name))
        serializer = ProductSerializers(products,many=True)
        return Response(serializer.data)
    else:
        return Response({'products',[]})