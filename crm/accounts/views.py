from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to the home page')

def contact(request):
    return HttpResponse('Contact us!')

def products(request):
    return HttpResponse('Our products are here')

def accounts(request):
    return HttpResponse('Customer accounts management')