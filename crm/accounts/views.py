from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import OrderForm

from .models import *

import logging
logger = logging.getLogger(__name__)


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


def create_order(request):
    form = OrderForm()
    
    if request.method == 'POST':
        
        logging.info(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/order_form.html', context)