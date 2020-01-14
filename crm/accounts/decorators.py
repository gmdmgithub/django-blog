from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.conf import settings

import logging

def unauthenticated_user(view_func):
    """"decorator checks if user is authenticated - only unauthenticated user are allowed to access"""
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect(reverse_lazy(settings.HOME_PAGE_URL))
        return view_func(request,*args, **kwargs)

    return wrapper_func


def restrict_view(allowed_roles=[]):
    """"decorator for checking groups"""
    
    def view_decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            for g in request.user.groups.all():
                if g.name in allowed_roles:
                    return view_func(request,*args, **kwargs)
            logging.info(f'User {request.user} does not have group {allowed_roles} - consider future problems his roles {request.user.groups.all()} , {request.path}')
            return redirect(reverse_lazy('contact'))
            
        return wrapper_func
    
    return view_decorator