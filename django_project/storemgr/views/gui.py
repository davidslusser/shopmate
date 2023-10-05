from django.views.generic import DetailView
from djangoaddicts.pygwalker.views import PygWalkerListView, PygWalkerPaginatedListView
from handyhelpers.views import HandyHelperActionView, HandyHelperIndexView

# import forms
from storemgr.forms import (
    FilterBrandForm,
    FilterCustomerForm,
    FilterManufacturerForm,
    FilterOrderForm,
    FilterProductForm,
)

# import models
from storemgr.models import Brand, Customer, Manufacturer, Order, Product


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
            "description": "ShopMate administrator portal",
        },
        {
            "url": "/admin",
            "icon": "fab fa-python",
            "title": "Django Console",
            "description": "Access the django administration page",
        },
    ]
    protected_group_name = "admin"


class AdminPanel(HandyHelperActionView):
    """render the storemgr index page"""

    title = '<span class="text-primary">Shop</span><span class="text-secondary">Mate</span> Admin Panel'
    subtitle = ""
    item_list = [
        {
            # "url": "/storemgr/create_manufacturer",
            "hx_get": "/storemgr/create_manufacturer",
            "icon": """<i class="fa-solid fa-industry"></i>""",
            "title": "Create Manufacturer",
            "description": "Create a new manufacturer",
        },
        {
            "hx_get": "/storemgr/create_brand",
            "icon": """<i class="fa-solid fa-language"></i>""",
            "title": "Create Brand",
            "description": "Create a new brand",
        },
        {
            "hx_get": "/storemgr/create_product",
            "icon": """<i class="fa-brands fa-product-hunt"></i>""",
            "title": "Create Product",
            "description": "Create a new product",
        },
        {
            "hx_get": "/storemgr/create_product_attribute",
            "icon": """<i class="fa-solid fa-swatchbook"></i>""",
            "title": "Create Attribute",
            "description": "Create a new product attribute",
        },
    ]


class ListBrands(PygWalkerListView):
    """list available Brand entries"""

    queryset = Brand.objects.all().select_related("manufacturer")
    title = "Brands"
    table = "storemgr/table/brands.htm"
    pygwalker_url = "/storemgr/analyze_brands/"

    filter_form_obj = FilterBrandForm
    filter_form_title = "<b>Filter Brands: </b>"
    filter_form_modal = "filter_brands"
    filter_form_tool_tip = "filter brands"


class ListCustomers(PygWalkerListView):
    """list available Customer entries"""

    queryset = Customer.objects.all()
    title = "Customers"
    table = "storemgr/table/customers.htm"
    pygwalker_url = "/storemgr/analyze_customers/"

    filter_form_obj = FilterCustomerForm
    filter_form_title = "<b>Filter Customers: </b>"
    filter_form_modal = "filter_customers"
    filter_form_tool_tip = "filter customers"


class ListManufacturers(PygWalkerListView):
    """list available Manufacturer entries"""

    queryset = Manufacturer.objects.all()
    title = "Manufacturers"
    table = "storemgr/table/manufacturers.htm"
    pygwalker_url = "/storemgr/analyze_manufacturers/"

    filter_form_obj = FilterManufacturerForm
    filter_form_title = "<b>Filter Manufacturers: </b>"
    filter_form_modal = "filter_manufacturers"
    filter_form_tool_tip = "filter manufacturers"


class ListOrders(PygWalkerPaginatedListView):
    """list available Order entries"""

    queryset = Order.objects.all().select_related("status", "customer").prefetch_related("products")
    title = "Orders"
    table = "storemgr/table/orders.htm"
    pygwalker_url = "/storemgr/analyze_orders/"

    filter_form_obj = FilterOrderForm
    filter_form_title = "<b>Filter Orders: </b>"
    filter_form_modal = "filter_orders"
    filter_form_tool_tip = "filter orders"


class ListProducts(PygWalkerListView):
    """list available Product entries"""

    queryset = Product.objects.all().prefetch_related("attributes")
    title = "Products"
    table = "storemgr/table/products.htm"
    pygwalker_url = "/storemgr/analyze_products/"

    filter_form_obj = FilterProductForm
    filter_form_title = "<b>Filter Products: </b>"
    filter_form_modal = "filter_products"
    filter_form_tool_tip = "filter products"


class DetailBrand(DetailView):
    model = Brand
    template_name = "storemgr/detail/brand.html"


class DetailCustomer(DetailView):
    model = Customer
    template_name = "storemgr/detail/customer.html"


class DetailManufacturer(DetailView):
    model = Manufacturer
    template_name = "storemgr/detail/manufacturer.html"


class DetailProduct(DetailView):
    model = Product
    template_name = "storemgr/detail/product.html"


class DetailOrder(DetailView):
    model = Order
    template_name = "storemgr/detail/order.html"
