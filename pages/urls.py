from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_company, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]