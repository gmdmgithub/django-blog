import django_filters

from django.forms import DateInput

from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="date_created", 
                            lookup_expr='gte',
                            label='Created from',
                            widget = DateInput(attrs={
                                        'class': 'datepicker', 
                                        'type':'date'}
                                    ))
    end_date = DateFilter(field_name="date_created", 
                            lookup_expr='lte', 
                            label='Created to',
                            widget = DateInput(attrs={
                                        'class': 'datepicker',  
                                        'type':'date'}
                                    ))
    number = CharFilter(field_name='number', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']