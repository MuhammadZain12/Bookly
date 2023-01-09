from django.contrib import admin
from .models import User,Hotel,Room,Booking

# Register your models here.

class UserModel(admin.ModelAdmin):
  list_display=(
    'name',
    'email',
    'cnic',
    'is_verified'
  )
  list_filter=('is_verified',)
  list_editable=['is_verified',]
  search_fields=['email','cnic']

class HotelModel(admin.ModelAdmin):
  list_display=['id','name','city']
  list_filter=['city',]
  search_fields=['name',]
  


class RoomModel(admin.ModelAdmin):
  list_display=['id','type','hotel','is_available']
  list_editable=['is_available',]
  list_filter=['is_available',]
  search_fields=['id','type']

class BookingModel(admin.ModelAdmin):
  list_display=['room','hotel','user','nights','is_verified']
  list_editable=['is_verified',]
  list_filter=['is_verified',]
  search_fields=['user',]


admin.site.register(User,UserModel)
admin.site.register(Hotel,HotelModel)
admin.site.register(Room,RoomModel)
admin.site.register(Booking,BookingModel)
admin.site.site_header="Bookly Admin Pannel"
admin.site.index_title="Welcome to Bookly Admin Pannel"
