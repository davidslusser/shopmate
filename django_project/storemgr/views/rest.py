""" DRF viewsets for applicable app models """

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from handyhelpers.drf_permissions import InAnyGroup

# import models
from storemgr.models import Brand, Customer, Invoice, Order, OrderStatus, Product, ProductAttribute

# import serializers
from storemgr.serializers import (
    BrandSerializer,
    CustomerSerializer,
    InvoiceSerializer,
    OrderSerializer,
    OrderStatusSerializer,
    ProductSerializer,
    ProductAttributeSerializer,
)

# import filtersets
from storemgr.filtersets import (
    BrandFilterSet,
    CustomerFilterSet,
    InvoiceFilterSet,
    OrderFilterSet,
    OrderStatusFilterSet,
    ProductFilterSet,
    ProductAttributeFilterSet,
)


class BrandViewSet(viewsets.ModelViewSet):
# class BrandViewSet(viewsets.ModelViewSet, InAnyGroup):
    """API endpoint that allows Brands to be viewed"""
    # permission_classes = (InAnyGroup,)
    # permission_dict = {'GET': ['blah'],
    #                    'POST': ['admin', 'orderers']}

    model = Brand
    queryset = model.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilterSet

    @action(detail=True, methods=["get"])
    def product_set(self, request, *args, **kwargs):
        """get the products associated with this Brand instance if available"""
        instance = self.get_object()
        data = instance.product_set.all()
        if data:
            try:
                serializer = ProductSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No products available for this brand ", status.HTTP_404_NOT_FOUND)


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Customers to be viewed"""

    model = Customer
    queryset = model.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilterSet

    @action(detail=True, methods=["get"])
    def order_set(self, request, *args, **kwargs):
        """get the orders associated with this Customer instance if available"""
        instance = self.get_object()
        data = instance.order_set.all()
        if data:
            try:
                serializer = OrderSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No orders available for this customer ", status.HTTP_404_NOT_FOUND)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Invoices to be viewed"""

    model = Invoice
    serializer_class = InvoiceSerializer
    filterset_class = InvoiceFilterSet

    def get_queryset(self):
        queryset = self.model.objects.all().select_related(
            "order",
            "product",
        )

        if is_expanded(self.request, "order"):
            queryset = queryset.select_related(
                "order__status",
                "order__customer",
            )

        if is_expanded(self.request, "product"):
            queryset = queryset.select_related(
                "product__brand",
            )

        return queryset


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Orders to be viewed"""

    model = Order
    serializer_class = OrderSerializer
    filterset_class = OrderFilterSet

    @action(detail=True, methods=["get"])
    def invoice_set(self, request, *args, **kwargs):
        """get the invoices associated with this Order instance if available"""
        instance = self.get_object()
        data = instance.invoice_set.all()
        if data:
            try:
                serializer = InvoiceSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No invoices available for this order ", status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["get"])
    def products(self, request, *args, **kwargs):
        """get the products associated with this Order instance if available"""
        instance = self.get_object()
        data = instance.products.all()
        if data:
            try:
                serializer = ProductSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No products available for this order ", status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        queryset = self.model.objects.all().select_related(
            "customer",
            "status",
        )

        if is_expanded(self.request, "customer"):
            queryset = queryset.select_related("customer")

        if is_expanded(self.request, "status"):
            queryset = queryset.select_related("status")

        return queryset


class OrderStatusViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows OrderStatuss to be viewed"""

    model = OrderStatus
    queryset = model.objects.all()
    serializer_class = OrderStatusSerializer
    filterset_class = OrderStatusFilterSet

    @action(detail=True, methods=["get"])
    def order_set(self, request, *args, **kwargs):
        """get the orders associated with this OrderStatus instance if available"""
        instance = self.get_object()
        data = instance.order_set.all()
        if data:
            try:
                serializer = OrderSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No orders available for this orderstatus ", status.HTTP_404_NOT_FOUND)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Products to be viewed"""

    model = Product
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet

    @action(detail=True, methods=["get"])
    def invoice_set(self, request, *args, **kwargs):
        """get the invoices associated with this Product instance if available"""
        instance = self.get_object()
        data = instance.invoice_set.all()
        if data:
            try:
                serializer = InvoiceSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No invoices available for this product ", status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["get"])
    def order_set(self, request, *args, **kwargs):
        """get the orders associated with this Product instance if available"""
        instance = self.get_object()
        data = instance.order_set.all()
        if data:
            try:
                serializer = OrderSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No orders available for this product ", status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=["get"])
    def attributes(self, request, *args, **kwargs):
        """get the attributess associated with this Product instance if available"""
        instance = self.get_object()
        data = instance.attributes.all()
        if data:
            try:
                serializer = ProductAttributeSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No attributess available for this product ", status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        queryset = self.model.objects.all().select_related(
            "brand",
        )

        if is_expanded(self.request, "brand"):
            queryset = queryset.select_related("brand")

        return queryset


class ProductAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows ProductAttributes to be viewed"""

    model = ProductAttribute
    queryset = model.objects.all()
    serializer_class = ProductAttributeSerializer
    filterset_class = ProductAttributeFilterSet

    @action(detail=True, methods=["get"])
    def product_set(self, request, *args, **kwargs):
        """get the products associated with this ProductAttribute instance if available"""
        instance = self.get_object()
        data = instance.product_set.all()
        if data:
            try:
                serializer = ProductSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No products available for this productattribute ", status.HTTP_404_NOT_FOUND)
