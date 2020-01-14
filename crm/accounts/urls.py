"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponse
from django.conf import settings

from . import views


urlpatterns = [
    
    path('login', views.login_user, name=settings.LOGIN_PAGE_URL),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),

    path('', views.home, name=settings.HOME_PAGE_URL),

    path('about/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk>/', views.accounts, name='customer'),
    
    path('create_order', views.create_order, name='new_order'),
    path('customer_orders/<str:fk>', views.create_customer_orders, name='customer_orders'),
    path('update_order/<str:pk>', views.update_order, name='upd_order'),
    path('delete_order/<str:pk>', views.delete_order, name='del_order'),
]