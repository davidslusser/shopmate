from django.urls import path
from storemgr.views import analysis, gui, htmx, report, test

urlpatterns = [
    # GUI views
    path("", gui.Index.as_view(), name=""),
    path("index", gui.Index.as_view(), name="index"),
    path("default", gui.Index.as_view(), name="default"),
    path("home", gui.Index.as_view(), name="home"),
    path("test", test.TestView.as_view(), name="test"),
    path("get_modal", test.GetModal.as_view(), name="get_modal"),
    path("admin_panel", gui.AdminPanel.as_view(), name="admin_panel"),
    path("annual_progress/", report.StoreMgrAnnualProgressView.as_view(), name="annual_progress"),
    path("annual_stats/", report.StoreMgrAnnualStatView.as_view(), name="annual_stats"),
    path("annual_trends/", report.StoreMgrAnnualTrendView.as_view(), name="annual_trends"),
    path("dashboard/", report.StoreMgrDashboard.as_view(), name="dashboard"),
    path("list_brands/", gui.ListBrands.as_view(), name="list_brands"),
    path("list_customers/", gui.ListCustomers.as_view(), name="list_customers"),
    path("list_manufacturers/", gui.ListManufacturers.as_view(), name="list_manufacturers"),
    path("list_orders/", gui.ListOrders.as_view(), name="list_orders"),
    path("list_products/", gui.ListProducts.as_view(), name="list_products"),
    path("detail_brand/<int:pk>", gui.DetailBrand.as_view(), name="detail_brand"),
    path("detail_customer/<int:pk>", gui.DetailCustomer.as_view(), name="detail_customer"),
    path("detail_manufacturer/<int:pk>", gui.DetailManufacturer.as_view(), name="detail_manufacturer"),
    path("detail_order/<str:pk>", gui.DetailOrder.as_view(), name="detail_order"),
    path("detail_product/<str:pk>", gui.DetailProduct.as_view(), name="detail_product"),
    path("analyze_brands/", analysis.AnalyzeBrands.as_view(), name="analyze_brands"),
    path("analyze_customers/", analysis.AnalyzeCustomers.as_view(), name="analyze_customers"),
    path("analyze_manufacturers/", analysis.AnalyzeManufacturers.as_view(), name="analyze_manufacturers"),
    path("analyze_orders/", analysis.AnalyzeOrders.as_view(), name="analyze_orders"),
    path("analyze_products/", analysis.AnalyzeProducts.as_view(), name="analyze_products"),
    # htmx views
    path("create_brand/", htmx.CreateBrandModalView.as_view(), name="create_brand"),
    path("create_manufacturer/", htmx.CreateManufacturerModalView.as_view(), name="create_manufacturer"),
    path("create_product/", htmx.CreateProductModalView.as_view(), name="create_product"),
    path("create_product_attribute/", htmx.CreateProductAttributeModalView.as_view(), name="create_product_attribute"),
]
