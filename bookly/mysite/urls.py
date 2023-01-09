from django.urls import path,re_path
from . import views

app_name='mysite'

urlpatterns=[
  path('home/',views.HomeView.as_view(),name='home'),
  re_path(r'^(?P<city>\w+)/hotels/$',views.CityView.as_view(),name='hotels'),
  re_path(r'^(?P<city>\w+)/hotels/(?P<hotel>\w+)/rooms/(?P<room>\w+)/',views.RoomView.as_view(),name='room'),
  re_path(r'^(?P<city>\w+)/hotels/(?P<id>\w+)/',views.HotelView.as_view(),name='hotel'),
 
  # path('user/',views.VerifyAccount.as_view(),name='verify'),
]