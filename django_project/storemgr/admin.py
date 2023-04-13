from django.contrib import admin

# import models
from storemgr.models import (ProductAttribute,
                             Brand,
                             Product,
                             OrderStatus,
                             Customer,
                             Order,
                             Invoice
                             )


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'key', 'value']
    search_fields = ['id', 'key', 'value']
    list_filter = []


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name', 'enabled']
    search_fields = ['id', 'name']
    list_filter = ['enabled']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'sku', 'brand', 'description', 'enabled']
    search_fields = ['sku', 'description']
    list_filter = ['brand', 'enabled']


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name']
    search_fields = ['id', 'name']
    list_filter = []


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'customer_id', 'first_name', 'last_name', 'email']
    search_fields = ['customer_id', 'first_name', 'last_name', 'email']
    list_filter = []


class OrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'order_id', 'status', 'customer']
    search_fields = ['order_id']
    list_filter = ['status', 'customer']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'order', 'product', 'qty']
    search_fields = ['id', 'qty']
    list_filter = ['order', 'product']


# register models
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
