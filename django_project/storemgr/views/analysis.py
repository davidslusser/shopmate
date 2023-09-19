from djangoaddicts.pygwalker.views import PygWalkerView, StaticCsvPygWalkerView, DynamicCsvPygWalkerView
from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages
from handyhelpers.mixins.view_mixins import FilterByQueryParamsMixin

# import models
from storemgr.models import Brand, Customer, Manufacturer, Order, Product
import mimetypes


class AnalyzeOrder(PygWalkerView):
    queryset = Order.objects.all()
    title = "Order Data Analysis"
    theme = "light"
    field_list = ["status__name", "customer", "order_id", "created_at", "updated_at", "products"]


class AnalyzeBrand(PygWalkerView):
    field_list = ["name", "enabled", "manufacturer__name", "product"]
    queryset = Brand.objects.all()
    title = "Brand Data Analysis"
    theme = "light"


class AnalyzeCustomer(PygWalkerView):
    field_list = ["customer_id", "order__created_at", "order__products"]
    queryset = Customer.objects.all()
    title = "Customer Data Analysis"
    theme = "light"


class AnalyzeManufacturer(PygWalkerView):
    field_list = ["name", "enabled", "created_at", "updated_at"]
    queryset = Manufacturer.objects.all()
    title = "Manufacturer Data Analysis"
    theme = "light"


class AnalyzeProduct(PygWalkerView):
    field_list = ["sku", "brand", "brand__manufacturer__name", "enabled", "created_at", "updated_at"]
    queryset = Product.objects.all()
    title = "Product Data Analysis"
    theme = "light"


class StaticTestView(StaticCsvPygWalkerView):
    csv_file = "storemgr/views/data.csv"
    theme = "light"
    title = "Salary Data"
