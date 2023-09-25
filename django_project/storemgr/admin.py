from django.contrib import admin

# import models
from storemgr.models import (
    Brand,
    Customer,
    Invoice,
    Manufacturer,
    Order,
    OrderStatus,
    Product,
    ProductAttribute,
)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display: list = ["id", "key", "value", "created_at", "updated_at"]
    search_fields: list = ["id", "key", "value"]
    list_filter: list = []


class ManufacturerAdmin(admin.ModelAdmin):
    list_display: list = ["id", "name", "enabled", "created_at", "updated_at"]
    search_fields: list = ["id", "name"]
    list_filter: list = ["enabled"]


class BrandAdmin(admin.ModelAdmin):
    list_display: list = ["id", "name", "manufacturer", "enabled", "created_at", "updated_at"]
    search_fields: list = ["id", "name"]
    list_filter: list = ["enabled", "manufacturer"]


class ProductAdmin(admin.ModelAdmin):
    list_display: list = ["sku", "brand", "description", "enabled", "created_at", "updated_at"]
    search_fields: list = ["sku", "description"]
    list_filter: list = ["brand", "enabled"]


class OrderStatusAdmin(admin.ModelAdmin):
    list_display: list = ["id", "name", "created_at", "updated_at"]
    search_fields: list = ["id", "name"]
    list_filter: list = []


class CustomerAdmin(admin.ModelAdmin):
    list_display: list = ["customer_id", "first_name", "last_name", "email", "created_at", "updated_at"]
    search_fields: list = ["customer_id", "first_name", "last_name", "email"]
    list_filter: list = []


class OrderAdmin(admin.ModelAdmin):
    list_display: list = ["order_id", "status", "customer", "created_at", "updated_at"]
    search_fields: list = ["order_id"]
    list_filter: list = ["status", "customer"]


class InvoiceAdmin(admin.ModelAdmin):
    list_display: list = ["id", "order", "product", "created_at", "updated_at"]
    search_fields: list = ["id"]
    list_filter: list = ["order", "product"]


# register models
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
