from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

import stripe

from rest_framework import status,authentication,permissions
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
#!checkOut
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkOut(request):
    print('Request Data' , request.data)
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key=settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity')*item.get('product').price for item in serializer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount*100),
                currency='USD',
                description='Charge from Djackets',
                source=serializer.validated_data['stripe_token']
            )
            serializer.save(user=request.user,paid_amount=paid_amount)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#!OrderList
class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request,format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders,many=True)
        return Response(serializer.data)
    