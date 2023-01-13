from __future__ import absolute_import,unicode_literals

from .email import booking_requested_message

from celery.utils.log import get_task_logger

from celery import shared_task

print(__name__)
logger=get_task_logger(__name__)

@shared_task
def booking_requested_message_task(name,email,hotel,room_type,nights,price):
  logger.info("Email sent successfully")
  return booking_requested_message(name,email,hotel,room_type,nights,price)