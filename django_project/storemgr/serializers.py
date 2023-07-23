""" DRF serailizers for applicable app models """

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


# import models
from storemgr.models import Brand, Customer, Invoice, Order, OrderStatus, Product, ProductAttribute


class BrandSerializer(FlexFieldsModelSerializer):
    """serializer class for Brand"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = [
            "created_at",
            "enabled",
            "id",
            "name",
            "updated_at",
        ]


class CustomerSerializer(FlexFieldsModelSerializer):
    """serializer class for Customer"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Customer
        fields = [
            "created_at",
            "customer_id",
            "email",
            "first_name",
            "last_name",
            "updated_at",
        ]


class InvoiceSerializer(FlexFieldsModelSerializer):
    """serializer class for Invoice"""

    order = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Invoice
        fields = [
            "created_at",
            "id",
            "order",
            "product",
            "updated_at",
        ]

        expandable_fields = {
            "order": "storemgr.serializers.OrderSerializer",
            "product": "storemgr.serializers.ProductSerializer",
        }


class OrderSerializer(FlexFieldsModelSerializer):
    """serializer class for Order"""

    customer = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Order
        fields = [
            "created_at",
            "customer",
            "order_id",
            "status",
            "updated_at",
        ]

        expandable_fields = {
            "customer": "storemgr.serializers.CustomerSerializer",
            "status": "storemgr.serializers.OrderStatusSerializer",
        }


class OrderStatusSerializer(FlexFieldsModelSerializer):
    """serializer class for OrderStatus"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = OrderStatus
        fields = [
            "created_at",
            "id",
            "name",
            "updated_at",
        ]


class ProductSerializer(FlexFieldsModelSerializer):
    """serializer class for Product"""

    brand = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Product
        fields = [
            "brand",
            "created_at",
            "description",
            "enabled",
            "sku",
            "updated_at",
        ]

        expandable_fields = {
            "brand": "storemgr.serializers.BrandSerializer",
        }


class ProductAttributeSerializer(FlexFieldsModelSerializer):
    """serializer class for ProductAttribute"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = ProductAttribute
        fields = [
            "created_at",
            "id",
            "key",
            "updated_at",
            "value",
        ]
