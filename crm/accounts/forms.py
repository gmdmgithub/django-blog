from django.forms import ModelForm

from .models import *


class OrderForm():
    class Meta:
        model = Order
        fields = '__all__' # if some list ['customer','number']
