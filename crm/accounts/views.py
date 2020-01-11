from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from .forms import OrderForm

from .filters import OrderFilter

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
    # return HttpResponse('Contact us!')
    context = {'title':'Contact us'}
    return render(request, 'accounts/contact.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'p_list':products})

def accounts(request, pk):
    """additional parameter is passed to the func dynamically"""
    
    customer = get_object_or_404(Customer, id=pk)
    orders = customer.order_set.all()
    o_l = len(orders)

    order_filter = OrderFilter(request.GET,queryset=orders)
    orders = order_filter.qs

    context = {'customer':customer, 'orders':orders, 'o_l':o_l, 'order_filter':order_filter}
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

def create_customer_orders(request, fk):

    customer = Customer.objects.get(id=fk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status', 'number'), extra=5 )
    logging.info(f'Request to create orders for customer {customer} of id: {fk}')

    if request.method == 'POST':
        # logging.info(f'save by post is provided {request}')
        formset = OrderFormSet(request.POST, instance=customer)
        # logging.info(f'formset problem? {formset}')
        if formset.is_valid():
            logging.info(request.POST)
            formset.save()
            return redirect(f'/customers/{customer.id}')
    
    
    # form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    context = {'title':'Create orders for user', 
                    'customer':customer, 
                    'formset':formset }
    return render(request, 'accounts/user_orders.html',context)

def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        logging.info(request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        logging.info(f'Delete item: {request.POST}')
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'accounts/delete.html', context)

def login(request):
    context = {'title':'Login page'}

    return render(request,'accounts/login.html', context)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/login')

    form = UserCreationForm() 

    
    context = {'title':'Register page', 'form':form}
    return render(request,'accounts/register.html', context)