from django.db import models

from django.contrib.auth.models import User
import logging

import uuid

# Create your models here.

class Customer(models.Model):
    """ Model representing Customer """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    profile_img = models.ImageField(null=True,blank=True, default='default.jpg')
    email = models.CharField(max_length=200,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.name}'

    def __unicode__(self):
        return f'Customer: {self.name}'



# post_save.connect(update_profile,sender=User)

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('CAT1', 'Windows'),
        ('CAT2', 'Doors'),
        ('CAT3', 'Walls'),
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    description = models.TextField(max_length=4000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)
    
    def cat_value(self):
        for c in self.CATEGORY:
            if c[0] == self.category:
                return c[1]

        return None
    
    def __str__(self):
        return f'Product name: {self.name}'

    def __unicode__(self):
        return f'Product name: {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    STATUS = (
        ('PENDING', 'Pending'),
        ('UNDER_DELIVERY','Out in delivery'),
        ('DELIVERED', 'Delivered to the customer')
    )

    number = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def status_value(self):
        for s in self.STATUS:
            if s[0] == self.status:
                return s[1]

        return None

    def __str__(self):
        return f'Order: {self.number}'

    def __unicode__(self):
        return f'Order: {self.number}'
