from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Customer

import logging

def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        logging.info('Signal - customer created')

post_save.connect(create_customer,sender=User) # one way is to register, second decorator


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    
    if created == False:
        instance.customer.save()
        logging.info(f'Signal - customer updated {instance.customer.id} ')