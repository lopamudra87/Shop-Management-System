from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('customers/', views.customer_list, name='customer_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('sales/', views.sale_list, name='sale_list'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('reports/', views.report_view, name='report_view'),
]