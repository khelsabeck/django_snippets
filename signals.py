from django.db.models.signals import post_save #signals when users created
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import MyModel
import datetime

def updated_value_message(instance):
    message_body = f'Salutation, {instance.first_name} {instance.last_name}. You are have created a new so-and so ...'
    send_mail(  'Thank you for choosing X',            #   header
                message_body, 
                'sendingemail@sender.com',            #   sender
                [instance.email],     #   recipient
                False   )

# '''
# This is a function for insuring that when a thing is created, there is an email (new user)
# '''
# @receiver(post_save, sender=MyModel)
# def create_profile(sender, instance, created, **kwargs):
    # if created:
        # send message ...
     
# '''
# This is a function for insuring that when a user is changed, the profile changes
# '''
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.user_profile.save()