import logging

logger = logging.getLogger(__name__)


from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# def home(request):
#     return HttpResponse('Welcome to the home page')

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    
    total_customers = len(customers)
    total_orders = len(orders)

    delivered = len(orders.filter(status='DELIVERED'))

    pending = len(orders.filter(status='PENDING'))

    context = {'orders':orders, 'customers':customers, 
                't_c':total_customers, 't_o':total_orders, 't_od':delivered, 't_op':pending}
    return render(request,'accounts/dashboard.html', context)

def contact(request):
    return HttpResponse('Contact us!')

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'p_list':products})

def accounts(request, pk):
    """additional parameter is passed to the func dynamically"""
    
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    o_l = len(orders)
    context = {'customer':customer, 'orders':orders, 'o_l':o_l}

    return render(request,'accounts/customers.html', context)