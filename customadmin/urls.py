from django.urls import path
from . import views as customadmin_views, views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('orders/', views.all_orders, name='admin_orders'),
    path('users/', views.all_users, name='admin_users'),
    path('orders/edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('admin/users/', views.all_users, name='admin_users'),
    path('admin/users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('admin/users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('admin/users/create/', views.create_user, name='create_user'),
    path('admin/users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/services/', views.all_services, name='admin_services'),
    path('admin/services/add/', views.add_service, name='add_service'),
    path('admin/services/edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('admin/services/delete/<int:service_id>/', views.delete_service, name='delete_service'),
]
