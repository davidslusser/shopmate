from django.urls import path
from storemgr import views as gui
from storemgr import reports

urlpatterns = [
    # GUI views
    path("", gui.Index.as_view(), name=""),
    path("home", gui.Index.as_view(), name="home"),
    path("annual_progress/", reports.StoreMgrAnnualProgressView.as_view(), name="annual_progress"),
    path("annual_stats/", reports.StoreMgrAnnualStatView.as_view(), name="annual_stats"),
    path("annual_trends/", reports.StoreMgrAnnualTrendView.as_view(), name="annual_trends"),
    path("dashboard/", reports.StoreMgrDashboard.as_view(), name="dashboard"),
    path("list_brands/", gui.ListBrands.as_view(), name="list_brands"),
    path("list_customers/", gui.ListCustomers.as_view(), name="list_customers"),
    path("list_orders/", gui.ListOrders.as_view(), name="list_orders"),
    path("list_products/", gui.ListProducts.as_view(), name="list_products"),
    path("test/", gui.Test.as_view(), name="test"),
]
