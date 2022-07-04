from rest_framework import serializers
from .models import *
from product.serializers import *

#!MyOrderItemSerializer
class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializers()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

#!MyOrderSerializer
class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )



#!OrderItemSerializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['price','product','quantity']

#!OrderSerializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ["id","first_name","last_name","email","address","zipcode","place","phone","stripe_token","items"]
        
    def create(self,validated_data):#eyni vaxtda hem order hemde orderitem objecti yaratmaq
        items_data = validated_data.pop('items')  #!=>burdan donenn deyer OrderItem daki objectdir
        print('Items Data ', items_data)
        print('Validated Data ', validated_data)
        order = Order.objects.create(**validated_data)
        print('Order ', order)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order,**item_data)
        return order