from django.db import models

# Create your models here.

class Customer(models.Model):
    """ Model representing Customer """
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer {self.name}'

    def __unicode__(self):
        return None
