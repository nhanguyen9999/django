from django.urls import path
from . import views
from .views import get_products, get_category, get_customers, get_bills, get_bill_details, product_list_view
from .views import chart_view1, chart_view2, chart_view3, chart_view4, chart_view5, chart_view6, chart_view7, chart_view8, chart_view9, chart_view10, chart_view11, chart_view12

urlpatterns = [
    path("", views.home, name="home"),
    path('product-data-json/', views.product_data_json, name='product_data_json'),  # Thêm dòng này
    path('api/products/', get_products, name='api_products'),
    path('api/category/', get_category, name='api_category'),
    path('api/customers/', get_customers, name='api_customers'),
    path('api/bills/', get_bills, name='api_bills'),
    path('api/billlines/', get_bill_details, name='api_billlines'),
    path('products/', product_list_view, name='product_list'),
    path('chart/chart1/', chart_view1, name='chart_view1'),
    path('chart/chart2/', chart_view2, name='chart_view2'),
    path('chart/chart3/', chart_view3, name='chart_view3'),
    path('chart/chart4/', chart_view4, name='chart_view4'),
    path('chart/chart5/', chart_view5, name='chart_view5'),
    path('chart/chart6/', chart_view6, name='chart_view6'),
    path('chart/chart7/', chart_view7, name='chart_view7'),
    path('chart/chart8/', chart_view8, name='chart_view8'),
    path('chart/chart9/', chart_view9, name='chart_view9'),
    path('chart/chart10/', chart_view10, name='chart_view10'),
    path('chart/chart11/', chart_view11, name='chart_view11'),
    path('chart/chart12/', chart_view12, name='chart_view12'),
    path('chart/', views.index, name='index')
]