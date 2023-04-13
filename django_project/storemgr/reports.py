from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView

# import models
from storemgr.models import Brand, Customer, Order, Product


class StoreMgrAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list = [
        dict(
            title="Brands",
            queryset=Brand.objects.all(),
            dt_field="created_at",
            icon=Brand.get_icon(),
            list_view="/storemgr/list_brands",
        ),
        dict(
            title="Customers",
            queryset=Customer.objects.all(),
            dt_field="created_at",
            icon=Customer.get_icon(),
            list_view="/storemgr/list_customers",
        ),
        dict(
            title="Orders",
            queryset=Order.objects.all(),
            dt_field="created_at",
            icon=Order.get_icon(),
            list_view="/storemgr/list_orders",
        ),
        dict(
            title="Products",
            queryset=Product.objects.all(),
            dt_field="created_at",
            icon=Product.get_icon(),
            list_view="/storemgr/list_products",
        ),
    ]


class StoreMgrAnnualStatView(AnnualStatView):
    """ """

    dataset_list = [
        dict(
            title="Brands",
            queryset=Brand.objects.all(),
            dt_field="created_at",
            icon=Brand.get_icon(),
            list_view="/storemgr/list_brands",
        ),
        dict(
            title="Customers",
            queryset=Customer.objects.all(),
            dt_field="created_at",
            icon=Customer.get_icon(),
            list_view="/storemgr/list_customers",
        ),
        dict(
            title="Orders",
            queryset=Order.objects.all(),
            dt_field="created_at",
            icon=Order.get_icon(),
            list_view="/storemgr/list_orders",
        ),
        dict(
            title="Products",
            queryset=Product.objects.all(),
            dt_field="created_at",
            icon=Product.get_icon(),
            list_view="/storemgr/list_products",
        ),
    ]


class StoreMgrAnnualTrendView(AnnualTrendView):
    """ """

    dataset_list = [
        dict(
            title="Brands",
            queryset=Brand.objects.all(),
            dt_field="created_at",
            icon=Brand.get_icon(),
            list_view="/storemgr/list_brands",
        ),
        dict(
            title="Customers",
            queryset=Customer.objects.all(),
            dt_field="created_at",
            icon=Customer.get_icon(),
            list_view="/storemgr/list_customers",
        ),
        dict(
            title="Orders",
            queryset=Order.objects.all(),
            dt_field="created_at",
            icon=Order.get_icon(),
            list_view="/storemgr/list_orders",
        ),
        dict(
            title="Products",
            queryset=Product.objects.all(),
            dt_field="created_at",
            icon=Product.get_icon(),
            list_view="/storemgr/list_products",
        ),
    ]
