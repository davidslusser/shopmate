from django.shortcuts import render

from django.views.generic import View
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView
from handyhelpers.permissions import InAnyGroup

# import models
from storemgr.models import Brand, Customer, Order, Product

# import forms
from storemgr.forms import FilterOrderForm, FilterProductForm


class Index(HandyHelperIndexView):
    """render the storemgr index page"""
    title = 'Welcome to <span class="text-primary">Shop</span><span class="text-secondary">Mate</span>!'
    subtitle = "Select an option below to get started"
    item_list = [
        {
            "url": "/storemgr/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "View dashboard",
        },
        # {
        #     'url': '/search',
        #     'icon': 'fas fa-search',
        #     'title': 'Search',
        #     'description': 'Run custom searches',
        # },
        {
            "url": "/storemgr/api/",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List available RESTful APIs",
        },
    ]
    protected_item_list = [
        {
            "url": "/storemgr/admin_panel",
            "icon": "fas fa-id-card-alt",
            "title": "Admin",
            "description": "Administrator portal",
        },
        {
            "url": "/admin",
            "icon": "fab fa-python",
            "title": "Django Console",
            "description": "Access the django administrator console",
        },
    ]
    protected_group_name = "admin"


class ListBrands(HandyHelperListPlusCreateAndFilterView):
    """list available Brand entries"""
    queryset = Brand.objects.all()
    title = "Brands"
    page_description = ""
    table = "storemgr/table/brands.htm"


class ListCustomers(HandyHelperListPlusCreateAndFilterView):
    """list available Customer entries"""
    queryset = Customer.objects.all()
    title = "Customers"
    page_description = ""
    table = "storemgr/table/customers.htm"


class ListOrders(HandyHelperListPlusCreateAndFilterView):
    """list available Order entries"""
    queryset = Order.objects.all().select_related("status", "customer").prefetch_related("products")
    title = "Orders"
    page_description = ""
    table = "storemgr/table/orders.htm"

    filter_form_obj = FilterOrderForm
    filter_form_title = "<b>Filter Orders: </b><small> </small>"
    filter_form_modal = "filter_orders"
    filter_form_tool_tip = "filter orders"


class ListProducts(HandyHelperListPlusCreateAndFilterView):
    """list available Product entries"""
    queryset = Product.objects.all().prefetch_related("attributes")
    title = "Products"
    page_description = ""
    table = "storemgr/table/products.htm"

    filter_form_obj = FilterProductForm
    filter_form_title = "<b>Filter Products: </b><small> </small>"
    filter_form_modal = "filter_products"
    filter_form_tool_tip = "filter products"


from djangoaddicts.hostutils.views import ShowHost
class Test(ShowHost):
    """Display dashboard like page showing an overview of host data"""
    template_name = "storemgr/custom/test.html"
    title = "This is a new title"
