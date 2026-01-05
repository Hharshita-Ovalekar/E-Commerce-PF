from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('api/products/', views.product_list, name='product_list'),
    path('api/register/', views.register),
    path('api/login/', views.login),
    path('api/logout/', views.logout),

]
