from django.template import Library

register=Library()

def getUser(email,letter):
  return email.split(letter,1)[0]

def multiply(number1,number2):
  print(number1)
  print(number2)
  return number1*number2

def formId(word,number):
  return word+str(number)

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
register.filter('getUser',getUser)  
register.filter('formId',formId)
register.filter('multiply',multiply)