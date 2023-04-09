from django.db import models
from django_filters.rest_framework.filters import CharFilter
from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

# import models
from django.contrib.contenttypes.models import ContentType
from storemgr.models import (Customer,
                             Order,
                             OrderStatus,
                             Product,
                             ProductAttribute
                             )


class CustomerFilterSet(FilterSet):
    order = RelatedFilter('OrderFilterSet', field_name='order', queryset=Order.objects.all())
    has_order = BooleanFilter(field_name='order', lookup_expr='isnull', exclude=True)

    class Meta:
        model = Customer
        fields = {
            'created_at': '__all__',        
            'customer_id': '__all__',        
            'first_name': '__all__',        
            'last_name': '__all__',        
            'updated_at': '__all__',        
        }
        

class OrderFilterSet(FilterSet):
    customer = RelatedFilter('CustomerFilterSet', field_name='customer', queryset=Customer.objects.all())
    status = RelatedFilter('OrderStatusFilterSet', field_name='status', queryset=OrderStatus.objects.all())
    products = RelatedFilter('ProductFilterSet', field_name='products', queryset=Product.objects.all())
    has_products = BooleanFilter(field_name='products', lookup_expr='isnull', exclude=True)

    class Meta:
        model = Order
        fields = {
            'created_at': '__all__',        
            'customer': '__all__',        
            'order_id': '__all__',        
            'status': '__all__',        
            'updated_at': '__all__',        
        }
        

class OrderStatusFilterSet(FilterSet):
    order = RelatedFilter('OrderFilterSet', field_name='order', queryset=Order.objects.all())
    has_order = BooleanFilter(field_name='order', lookup_expr='isnull', exclude=True)

    class Meta:
        model = OrderStatus
        fields = {
            'created_at': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class ProductFilterSet(FilterSet):
    order = RelatedFilter('OrderFilterSet', field_name='order', queryset=Order.objects.all())
    has_order = BooleanFilter(field_name='order', lookup_expr='isnull', exclude=True)
    attributes = RelatedFilter('ProductAttributeFilterSet', field_name='attributes', queryset=ProductAttribute.objects.all())
    has_attributes = BooleanFilter(field_name='attributes', lookup_expr='isnull', exclude=True)

    class Meta:
        model = Product
        fields = {
            'created_at': '__all__',        
            'description': '__all__',        
            'sku': '__all__',        
            'updated_at': '__all__',        
        }
        

class ProductAttributeFilterSet(FilterSet):
    product = RelatedFilter('ProductFilterSet', field_name='product', queryset=Product.objects.all())
    has_product = BooleanFilter(field_name='product', lookup_expr='isnull', exclude=True)

    class Meta:
        model = ProductAttribute
        fields = {
            'created_at': '__all__',        
            'id': '__all__',        
            'key': '__all__',        
            'updated_at': '__all__',        
            'value': '__all__',        
        }
        