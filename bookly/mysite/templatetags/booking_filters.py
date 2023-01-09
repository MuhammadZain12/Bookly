from django.template import Library

register=Library()

def bookingCheck(booking_data,data_to_check):
  for booking in booking_data:
    if booking.room.id==data_to_check:
      return True 
  return False    


def isVerified(booking_data,data_to_check):
  for booking in booking_data:
    if booking.room.id==data_to_check:
      if booking.is_verified:
        return True
  return False

register.filter('bookingCheck',bookingCheck)  
register.filter('isVerified',isVerified)  