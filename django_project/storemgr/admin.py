from django.contrib import admin

# import models
from storemgr.models import ProductAttribute, Product, OrderStatus, Customer, Order


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "key", "value"]
    search_fields = ["id", "key", "value"]
    list_filter = []


class ProductAdmin(admin.ModelAdmin):
    list_display = ["created_at", "updated_at", "sku", "description"]
    search_fields = ["sku", "description"]
    list_filter = []


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name"]
    search_fields = ["id", "name"]
    list_filter = []


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "updated_at",
        "customer_id",
        "first_name",
        "last_name",
    ]
    search_fields = ["customer_id", "first_name", "last_name"]
    list_filter = []


class OrderAdmin(admin.ModelAdmin):
    list_display = ["created_at", "updated_at", "order_id", "status", "customer"]
    search_fields = ["order_id"]
    list_filter = ["status", "customer"]


# register models
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
