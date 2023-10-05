from djangoaddicts.pygwalker.views import PygWalkerView

# import models
from storemgr.models import Brand, Customer, Manufacturer, Order, Product


class AnalyzeOrders(PygWalkerView):
    queryset = Order.objects.all()
    field_list = [
        "order_id",
        "status__name",
        "customer",
        "created_at",
        "updated_at",
        "products",
        "products__brand__name",
    ]


class AnalyzeBrands(PygWalkerView):
    field_list = ["name", "enabled", "manufacturer__name", "product", "product__order"]
    queryset = Brand.objects.all()


class AnalyzeCustomers(PygWalkerView):
    field_list = [
        "customer_id",
        "order__created_at",
        "order__products",
        "order__products__brand__name",
        "created_at",
        "updated_at",
    ]
    queryset = Customer.objects.all()


class AnalyzeManufacturers(PygWalkerView):
    field_list = ["name", "enabled", "brand__product__order", "created_at", "updated_at"]
    queryset = Manufacturer.objects.all()


class AnalyzeProducts(PygWalkerView):
    field_list = ["sku", "brand__name", "brand__manufacturer__name", "order", "enabled", "created_at", "updated_at"]
    queryset = Product.objects.all()
