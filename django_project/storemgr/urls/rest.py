from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from storemgr.views import rest

router = routers.DefaultRouter()

# storemgr API Endpoints
router.register(r"brand", rest.BrandViewSet, "brand")
router.register(r"customer", rest.CustomerViewSet, "customer")
router.register(r"invoice", rest.InvoiceViewSet, "invoice")
router.register(r"order", rest.OrderViewSet, "order")
router.register(r"orderstatus", rest.OrderStatusViewSet, "orderstatus")
router.register(r"product", rest.ProductViewSet, "product")
router.register(r"productattribute", rest.ProductAttributeViewSet, "productattribute")

urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
]
