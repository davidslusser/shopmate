from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded

# import models
from storemgr.models import Customer, Order, OrderStatus, Product, ProductAttribute

# import serializers
from storemgr.serializers import (
    CustomerSerializer,
    OrderSerializer,
    OrderStatusSerializer,
    ProductSerializer,
    ProductAttributeSerializer,
)

# import filtersets
from storemgr.filtersets import (
    CustomerFilterSet,
    OrderFilterSet,
    OrderStatusFilterSet,
    ProductFilterSet,
    ProductAttributeFilterSet,
)


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
            return Response("No orders available for this customer ", status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Orders to be viewed"""

    model = Order
    serializer_class = OrderSerializer
    filterset_class = OrderFilterSet

    @action(detail=True, methods=["get"])
    def products(self, request, *args, **kwargs):
        """get the productss associated with this Order instance if available"""
        instance = self.get_object()
        data = instance.products.all()
        if data:
            try:
                serializer = ProductSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No productss available for this order ", status.HTTP_400_BAD_REQUEST)

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
            return Response("No orders available for this orderstatus ", status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows Products to be viewed"""

    model = Product
    queryset = model.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet

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
            return Response("No orders available for this product ", status.HTTP_400_BAD_REQUEST)

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
            return Response(
                "No attributess available for this product ",
                status.HTTP_400_BAD_REQUEST,
            )


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
            return Response(
                "No products available for this productattribute ",
                status.HTTP_400_BAD_REQUEST,
            )
