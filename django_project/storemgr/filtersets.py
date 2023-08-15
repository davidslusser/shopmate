""" filtersets for applicable app models """

from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

# import models
from storemgr.models import Brand, Customer, Invoice, Order, OrderStatus, Product, ProductAttribute


class BrandFilterSet(FilterSet):
    """filterset class for Brand"""

    product = RelatedFilter("ProductFilterSet", field_name="product", queryset=Product.objects.all())
    has_product = BooleanFilter(field_name="product", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = {
            "created_at": "__all__",
            "enabled": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
        }


class CustomerFilterSet(FilterSet):
    """filterset class for Customer"""

    order = RelatedFilter("OrderFilterSet", field_name="order", queryset=Order.objects.all())
    has_order = BooleanFilter(field_name="order", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Customer
        fields = {
            "created_at": "__all__",
            "customer_id": "__all__",
            "email": "__all__",
            "first_name": "__all__",
            "last_name": "__all__",
            "updated_at": "__all__",
        }


class InvoiceFilterSet(FilterSet):
    """filterset class for Invoice"""

    order = RelatedFilter("OrderFilterSet", field_name="order", queryset=Order.objects.all())
    product = RelatedFilter("ProductFilterSet", field_name="product", queryset=Product.objects.all())

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Invoice
        fields = {
            "created_at": "__all__",
            "id": "__all__",
            "order": "__all__",
            "product": "__all__",
            "updated_at": "__all__",
        }


class OrderFilterSet(FilterSet):
    """filterset class for Order"""

    customer = RelatedFilter("CustomerFilterSet", field_name="customer", queryset=Customer.objects.all())
    status = RelatedFilter("OrderStatusFilterSet", field_name="status", queryset=OrderStatus.objects.all())
    invoice = RelatedFilter("InvoiceFilterSet", field_name="invoice", queryset=Invoice.objects.all())
    has_invoice = BooleanFilter(field_name="invoice", lookup_expr="isnull", exclude=True)
    products = RelatedFilter("ProductFilterSet", field_name="products", queryset=Product.objects.all())
    has_products = BooleanFilter(field_name="products", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Order
        fields = {
            "created_at": "__all__",
            "customer": "__all__",
            "order_id": "__all__",
            "status": "__all__",
            "updated_at": "__all__",
        }


class OrderStatusFilterSet(FilterSet):
    """filterset class for OrderStatus"""

    order = RelatedFilter("OrderFilterSet", field_name="order", queryset=Order.objects.all())
    has_order = BooleanFilter(field_name="order", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = OrderStatus
        fields = {
            "created_at": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
        }


class ProductFilterSet(FilterSet):
    """filterset class for Product"""

    brand = RelatedFilter("BrandFilterSet", field_name="brand", queryset=Brand.objects.all())
    invoice = RelatedFilter("InvoiceFilterSet", field_name="invoice", queryset=Invoice.objects.all())
    has_invoice = BooleanFilter(field_name="invoice", lookup_expr="isnull", exclude=True)
    order = RelatedFilter("OrderFilterSet", field_name="order", queryset=Order.objects.all())
    has_order = BooleanFilter(field_name="order", lookup_expr="isnull", exclude=True)
    attributes = RelatedFilter(
        "ProductAttributeFilterSet", field_name="attributes", queryset=ProductAttribute.objects.all()
    )
    has_attributes = BooleanFilter(field_name="attributes", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Product
        fields = {
            "brand": "__all__",
            "created_at": "__all__",
            "description": "__all__",
            "enabled": "__all__",
            "sku": "__all__",
            "updated_at": "__all__",
        }


class ProductAttributeFilterSet(FilterSet):
    """filterset class for ProductAttribute"""

    product = RelatedFilter("ProductFilterSet", field_name="product", queryset=Product.objects.all())
    has_product = BooleanFilter(field_name="product", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = ProductAttribute
        fields = {
            "created_at": "__all__",
            "id": "__all__",
            "key": "__all__",
            "updated_at": "__all__",
            "value": "__all__",
        }
