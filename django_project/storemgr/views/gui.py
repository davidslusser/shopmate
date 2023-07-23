from django.shortcuts import render

from django.views.generic import DetailView, View
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView
from handyhelpers.permissions import InAnyGroup

# import models
from storemgr.models import Brand, Customer, Manufacturer, Order, Product

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
            "url": "/storemgr/rest/",
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
    queryset = Brand.objects.all().select_related("manufacturer")
    title = "Brands"
    table = "storemgr/table/brands.htm"


class ListCustomers(HandyHelperListPlusCreateAndFilterView):
    """list available Customer entries"""
    queryset = Customer.objects.all()
    title = "Customers"
    table = "storemgr/table/customers.htm"


class ListManufacturers(HandyHelperListPlusCreateAndFilterView):
    """list available Manufacturer entries"""
    queryset = Manufacturer.objects.all()
    title = "Manufacturers"
    table = "storemgr/table/manufacturers.htm"


class ListOrders(HandyHelperListPlusCreateAndFilterView):
    """list available Order entries"""
    queryset = Order.objects.all().select_related("status", "customer").prefetch_related("products")
    title = "Orders"
    table = "storemgr/table/orders.htm"

    filter_form_obj = FilterOrderForm
    filter_form_title = "<b>Filter Orders: </b>"
    filter_form_modal = "filter_orders"
    filter_form_tool_tip = "filter orders"


class ListProducts(HandyHelperListPlusCreateAndFilterView):
    """list available Product entries"""
    queryset = Product.objects.all().prefetch_related("attributes")
    title = "Products"
    table = "storemgr/table/products.htm"

    filter_form_obj = FilterProductForm
    filter_form_title = "<b>Filter Products: </b>"
    filter_form_modal = "filter_products"
    filter_form_tool_tip = "filter products"


class DetailBrand(DetailView):
    model = Brand
    template_name = 'storemgr/detail/brand.html'
    # context_object_name = 'brand'


class DetailCustomer(DetailView):
    model = Customer
    template_name = 'storemgr/detail/customer.html'


class DetailManufacturer(DetailView):
    model = Manufacturer
    template_name = 'storemgr/detail/manufacturer.html'
    # context_object_name = 'brand'


class DetailProduct(DetailView):
    model = Product
    template_name = 'storemgr/detail/product.html'


class DetailOrder(DetailView):
    model = Order
    template_name = 'storemgr/detail/order.html'
