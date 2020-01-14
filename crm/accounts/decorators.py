from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

import logging

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return view_func(request,*args, **kwargs)

    return wrapper_func


def restrict_view(allowed_roles=[]):
    def view_decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            logging.info(allowed_roles)
            logging.info(request.user.groups)
            if request.user.groups.exists():
                
                for g in request.user.groups.all():
                    if g in allowed_roles:
                        return view_func(request,*args, **kwargs)
                
            return redirect(reverse_lazy('contact'))
            
        return wrapper_func
    
    return view_decorator