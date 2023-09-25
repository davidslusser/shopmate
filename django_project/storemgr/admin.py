from django.contrib import admin

# import models
from storemgr.models import (Brand, Customer, Invoice, Manufacturer, Order,
                             OrderStatus, Product, ProductAttribute)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ["id", "key", "value", "created_at", "updated_at"]
    search_fields = ["id", "key", "value"]
    list_filter = []


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "enabled", "created_at", "updated_at"]
    search_fields = ["id", "name"]
    list_filter = ["enabled"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "manufacturer", "enabled", "created_at", "updated_at"]
    search_fields = ["id", "name"]
    list_filter = ["enabled", "manufacturer"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["sku", "brand", "description", "enabled", "created_at", "updated_at"]
    search_fields = ["sku", "description"]
    list_filter = ["brand", "enabled"]


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    search_fields = ["id", "name"]
    list_filter = []


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "first_name", "last_name", "email", "created_at", "updated_at"]
    search_fields = ["customer_id", "first_name", "last_name", "email"]
    list_filter = []


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "status", "customer", "created_at", "updated_at"]
    search_fields = ["order_id"]
    list_filter = ["status", "customer"]


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product", "created_at", "updated_at"]
    search_fields = [
        "id",
    ]
    list_filter = ["order", "product"]


# register models
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
