from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from storemgr import viewsets

app_name = "storemgr"

router = routers.DefaultRouter()

# storemgr API Endpoints
router.register(r"customer", viewsets.CustomerViewSet, "customer")
router.register(r"order", viewsets.OrderViewSet, "order")
router.register(r"orderstatus", viewsets.OrderStatusViewSet, "orderstatus")
router.register(r"product", viewsets.ProductViewSet, "product")
router.register(
    r"productattribute", viewsets.ProductAttributeViewSet, "productattribute"
)


urlpatterns = [
    # API views
    path("api/", include(router.urls)),
]
