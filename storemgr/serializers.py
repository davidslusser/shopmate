from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


# import models
from storemgr.models import (Customer,
                             Order,
                             OrderStatus,
                             Product,
                             ProductAttribute
                             )


class CustomerSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'created_at',
            'customer_id',
            'first_name',
            'last_name',
            'updated_at',
        ]
        

class OrderSerializer(FlexFieldsModelSerializer):
    customer = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = [
            'created_at',
            'customer',
            'order_id',
            'status',
            'updated_at',
        ]
        
        expandable_fields = {
            'customer': 'storemgr.serializers.CustomerSerializer',
            'status': 'storemgr.serializers.OrderStatusSerializer',
        }
        

class OrderStatusSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = OrderStatus
        fields = [
            'created_at',
            'id',
            'name',
            'updated_at',
        ]
        

class ProductSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Product
        fields = [
            'created_at',
            'description',
            'sku',
            'updated_at',
        ]
        

class ProductAttributeSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = [
            'created_at',
            'id',
            'key',
            'updated_at',
            'value',
        ]
        