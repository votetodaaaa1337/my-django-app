from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('create/<int:service_id>/', views.create_order, name='create_order'),
    path('my/', views.my_orders, name='my_orders'),
    path('worker/', views.worker_dashboard, name='worker_dashboard'),
    path('update/<int:order_id>/', views.update_order_status, name='update_order'),
    path('order/<int:service_id>/', order_create, name='order_create'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('worker/', views.worker_orders, name='worker_orders'),
    path('worker/<int:order_id>/', views.worker_order_detail, name='worker_order_detail'),
    path('no-access/', views.no_access, name='no_access'),
    path('available/', views.available_orders, name='available_orders'),
    path('accept/<int:order_id>/', views.accept_order, name='accept_order'),
]
