from django.db import models

import uuid

# Create your models here.

class Customer(models.Model):
    """ Model representing Customer """
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.name}'

    def __unicode__(self):
        return None
class Product(models.Model):
    CATEGORY = (
        ('CAT1', 'Windows'),
        ('CAT2', 'Doors'),
        ('CAT3', 'Walls'),
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    description = models.CharField(max_length=4000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product name: {self.name}'

    def __unicode__(self):
        return f'Product name: {self.name}'

class Order(models.Model):
    # customer =
    # product=
    STATUS = (
        ('PENDING', 'Pending'),
        ('UNDER_DELIVERY','Out in delivery'),
        ('DELIVERED', 'Delivered to the customer')
    )

    number = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)


    def __str__(self):
        return f'Order: {self.number}'

    def __unicode__(self):
        return f'Order: {self.number}'
