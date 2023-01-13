from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings


def booking_requested_message(name,email,hotel,room_type,nights,price):
  print('came here')
  context={
    'name':name,
    'email':email,
    'hotel':hotel,
    'room':room_type,
    'nights':nights,
    'price':price,
  }

  email_subject="Thank You For Using Bookly"
  email_body=render_to_string('booking_requested_message.txt',context)
  return send_mail(email_subject,email_body,settings.DEFAULT_FROM_EMAIL,[email,])

