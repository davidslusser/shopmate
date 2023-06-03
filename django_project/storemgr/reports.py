from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView
from handyhelpers.views.report import (get_colors, build_day_week_month_year_charts, get_timestamps)

# import models
from storemgr.models import (Brand, Customer, Order, OrderStatus, Product)


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


class StoreMgrDashboard(View):
    """ """
    title = 'Annual Progress Report'
    sub_title = 'cumulative data added over the past year'
    template_name = 'storemgr/custom/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        """ """
        context = {}
        context['counts'] = [
            {"title": "Brands", 
             "count": Brand.objects.filter(enabled=True).count(), 
             "icon": Brand.get_icon(), 
             "link": "/storemgr/list_brands/?enabled=True"},
            
            {"title": "Customers", 
             "count": Customer.objects.filter().count(), 
             "icon": Customer.get_icon(), 
             "link": "/storemgr/list_customers/"},
            
            {"title": "Products", 
             "count": Product.objects.filter(enabled=True).count(), 
             "icon": Product.get_icon(), 
             "link": "/storemgr/list_products/?enabled=True"},
            
            {"title": "Orders", 
             "count": Order.objects.filter().count(), 
             "icon": Order.get_icon(), 
             "link": "/storemgr/list_orders/"},
            ]

        # get Orders by brand
        brand_list = [i.name for i in Brand.objects.all()]
        context['orders_by_brand'] = dict(
            id='orders_by_brand',
            type='bar',
            label_list=brand_list,
            value_list=[Order.objects.filter(**{'products__brand__name': brand}).count() for brand in brand_list],
            list_view='/storemgr/list_orders?products__brand__name=',
            color_list=get_colors(len(brand_list)),
        )
        
        # get Orders by status
        status_list = [i.name for i in OrderStatus.objects.all()]
        context['orders_by_status'] = dict(
            id='orders_by_status',
            type='pie',
            label_list=status_list,
            value_list=[Order.objects.filter(**{'status__name': status}).count() for status in status_list],
            list_view='/storemgr/list_orders?status__name=',
            color_list=get_colors(len(status_list)),
        )
                
        return render(request, self.template_name, context=context)
