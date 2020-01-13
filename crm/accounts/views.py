from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import OrderForm, CreateUserForm

from .filters import OrderFilter

from .models import *

import logging
logger = logging.getLogger(__name__)


# def home(request):
#     return HttpResponse('Welcome to the home page')

@login_required(login_url=reverse_lazy('login'))
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

@login_required(login_url=reverse_lazy('login'))
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'p_list':products})

@login_required(login_url=reverse_lazy('login'))
def accounts(request, pk):
    """additional parameter is passed to the func dynamically"""
    
    customer = get_object_or_404(Customer, id=pk)
    orders = customer.order_set.all()
    o_l = len(orders)

    order_filter = OrderFilter(request.GET,queryset=orders)
    orders = order_filter.qs

    context = {'customer':customer, 'orders':orders, 'o_l':o_l, 'order_filter':order_filter}
    return render(request,'accounts/customers.html', context)

@login_required(login_url=reverse_lazy('login'))
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

@login_required(login_url=reverse_lazy('login'))
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

@login_required(login_url=reverse_lazy('login'))
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

@login_required(login_url=reverse_lazy('login'))
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        logging.info(f'Delete item: {request.POST}')
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'accounts/delete.html', context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,f'User successfully login {username}')
            logging.info(f'user authenticated {username}')
            return redirect('/')
        else:
            logging.error(f'Problem with login {form.error_messages}')
            messages.error(request, 'Invalid/login password')
    
    form = AuthenticationForm() 
    context = {'title':'Login page', 'form':form}

    return render(request,'accounts/login.html', context)


def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'User successfully created for {username}')
            return redirect('/login')

    form = CreateUserForm() 

    
    context = {'title':'Register page', 'form':form}
    return render(request,'accounts/register.html', context)

@login_required(login_url=reverse_lazy('login'))
def logout_user(request):

    logout(request)

    return redirect('/')