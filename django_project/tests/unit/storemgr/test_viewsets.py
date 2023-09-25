import os

import django
from model_bakery import baker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
os.environ.setdefault("ENV_PATH", "../envs/.env.test")
django.setup()

from unittest.mock import patch

from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


def create_custom_client(group_name):
    """create a client user in a specified group and return a client for object for that user"""
    user = baker.make("auth.User", username=f"{group_name}_user")
    group = baker.make("auth.Group", name=group_name)
    user.groups.add(group)
    token = baker.make("authtoken.Token", user=user)
    client = APIClient()
    client.credentials(**dict(HTTP_AUTHORIZATION=f"Token {token.key}"))
    return client


class UserSetupMixin:
    def setUp(self):
        self.user = baker.make("auth.User", username="tester_basic")
        self.token = baker.make("authtoken.Token", user=self.user)
        self.client = APIClient()
        self.client.credentials(**dict(HTTP_AUTHORIZATION=f"Token {self.token.key}"))


class BrandTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the BrandViewSet viewset"""

    def setUp(self):
        super(BrandTests, self).setUp()
        self.row = baker.make("storemgr.Brand")

    def test_brand_list(self):
        """verify that a get request to the brand-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:brand-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_brand_retrieve(self):
        """verify that a get request to the brand-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:brand-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["id"]), getattr(self.row, "pk")

    def test_brand_product_set(self):
        """verify the brand-product-set endpoint returns a 200 and the row content is found"""
        # M2O
        product = baker.make("storemgr.Product", brand=self.row)
        url = reverse("storemgr:brand-product-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(product), response.content.decode("utf-8"))


class CustomerTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the CustomerViewSet viewset"""

    def setUp(self):
        super(CustomerTests, self).setUp()
        self.row = baker.make("storemgr.Customer")

    def test_customer_list(self):
        """verify that a get request to the customer-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:customer-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_customer_retrieve(self):
        """verify that a get request to the customer-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:customer-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["customer_id"]), getattr(self.row, "pk")

    def test_customer_order_set(self):
        """verify the customer-order-set endpoint returns a 200 and the row content is found"""
        # M2O
        order = baker.make("storemgr.Order", customer=self.row)
        url = reverse("storemgr:customer-order-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(order), response.content.decode("utf-8"))


class InvoiceTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the InvoiceViewSet viewset"""

    def setUp(self):
        super(InvoiceTests, self).setUp()
        self.row = baker.make("storemgr.Invoice")

    def test_invoice_list(self):
        """verify that a get request to the invoice-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:invoice-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_invoice_retrieve(self):
        """verify that a get request to the invoice-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:invoice-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["id"]), getattr(self.row, "pk")


class OrderTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the OrderViewSet viewset"""

    def setUp(self):
        super(OrderTests, self).setUp()
        self.row = baker.make("storemgr.Order")

    def test_order_list(self):
        """verify that a get request to the order-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:order-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_order_retrieve(self):
        """verify that a get request to the order-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:order-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["order_id"]), getattr(self.row, "pk")

    def test_order_invoice_set(self):
        """verify the order-invoice-set endpoint returns a 200 and the row content is found"""
        # M2O
        invoice = baker.make("storemgr.Invoice", order=self.row)
        url = reverse("storemgr:order-invoice-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(invoice), response.content.decode("utf-8"))

    def test_order_products(self):
        """verify the order-products endpoint returns a 200 and the row content is found"""
        # M2M
        product = baker.make("storemgr.Product")
        self.row.products.add(product)
        url = reverse("storemgr:order-products", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(product), response.content.decode("utf-8"))


class OrderStatusTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the OrderStatusViewSet viewset"""

    def setUp(self):
        super(OrderStatusTests, self).setUp()
        self.row = baker.make("storemgr.OrderStatus")

    def test_orderstatus_list(self):
        """verify that a get request to the orderstatus-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:orderstatus-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_orderstatus_retrieve(self):
        """verify that a get request to the orderstatus-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:orderstatus-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["id"]), getattr(self.row, "pk")

    def test_orderstatus_order_set(self):
        """verify the orderstatus-order-set endpoint returns a 200 and the row content is found"""
        # M2O
        order = baker.make("storemgr.Order", status=self.row)
        url = reverse("storemgr:orderstatus-order-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(order), response.content.decode("utf-8"))


class ProductTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the ProductViewSet viewset"""

    def setUp(self):
        super(ProductTests, self).setUp()
        self.row = baker.make("storemgr.Product")

    def test_product_list(self):
        """verify that a get request to the product-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:product-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_product_retrieve(self):
        """verify that a get request to the product-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:product-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["sku"]), getattr(self.row, "pk")

    def test_product_attributes(self):
        """verify the product-attributes endpoint returns a 200 and the row content is found"""
        # M2M
        productattribute = baker.make("storemgr.ProductAttribute")
        self.row.attributes.add(productattribute)
        url = reverse("storemgr:product-attributes", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(productattribute), response.content.decode("utf-8"))

    def test_product_invoice_set(self):
        """verify the product-invoice-set endpoint returns a 200 and the row content is found"""
        # M2O
        invoice = baker.make("storemgr.Invoice", product=self.row)
        url = reverse("storemgr:product-invoice-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(invoice), response.content.decode("utf-8"))

    def test_product_order_set(self):
        """verify the product-order-set endpoint returns a 200 and the row content is found"""
        # M2M
        order = baker.make("storemgr.Order")
        order.products.add(self.row)
        url = reverse("storemgr:product-order-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(order), response.content.decode("utf-8"))


class ProductAttributeTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the ProductAttributeViewSet viewset"""

    def setUp(self):
        super(ProductAttributeTests, self).setUp()
        self.row = baker.make("storemgr.ProductAttribute")

    def test_productattribute_list(self):
        """verify that a get request to the productattribute-list endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:productattribute-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_productattribute_retrieve(self):
        """verify that a get request to the productattribute-detail endpoint returns a 200 and the row content is found"""
        url = reverse("storemgr:productattribute-detail", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["id"]), getattr(self.row, "pk")

    def test_productattribute_product_set(self):
        """verify the productattribute-product-set endpoint returns a 200 and the row content is found"""
        # M2M
        product = baker.make("storemgr.Product")
        product.attributes.add(self.row)
        url = reverse("storemgr:productattribute-product-set", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(product), response.content.decode("utf-8"))
