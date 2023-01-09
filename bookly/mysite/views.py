
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views,login,authenticate,logout
from django.views.generic import TemplateView,View,ListView,DetailView
from pathlib import Path
from os import path
from django.urls import reverse_lazy,reverse
from mysite.models import Hotel,Room,Booking,User

# Create your views here.

####################  (Class Views) ######################
##Login View
class LoginView(views.LoginView):
  # success_url=reverse_lazy('mysite:home')
  def post(self, request, *args: str, **kwargs):
    email=request.POST["email"]
    password=request.POST["password"]
    user=authenticate(request=request,username=email,password=password)
    # try:
    #   user2=User.objects.get(username=username)
    #   print(user2)
      
    #   return render(request,'registration/login.html',context={'password':'• Incorrect Password'})
    # except:
    if user is not None:
      if user.is_verified:
        login(request=request,user=user)
        return redirect(reverse('mysite:home'))
      else:
        return render(request,'registration/login.html',context={'data':'• Your account has not been verified yet'}) 
    else:
      return render(request,'registration/login.html',context={'data':'• User does not exist'})
  
  def get(self, request, *args: str, **kwargs):
    return render(request,'registration/login.html',context={})


#View Of Home Page
class HomeView(View):
  def get(self,request,*args,**kwargs):
    cities=Hotel.objects.order_by('city').values('city').distinct()
    cities_names=[]
    for x in cities:
      cities_names.append(x['city'])
    print(cities_names) 
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # FINAL_DIR=path.join(BASE_DIR,'static\\mysite\\cities\\')
    FINAL_DIR='mysite/cities/'
    # paths=[]
    # for x in cities_names:
    #   # paths.append(path.join(FINAL_DIR,f'/{x}.jpg'))
    #   paths.append(FINAL_DIR+f'{x}.jpg')
    # cities_dict={}
    # for x in range(len(cities_names)):
    #   cities_dict[cities_names[x]]=paths[x]
    # print(cities_dict)    

    return render(request,'mysite/home.html',context={'title':'Home','cities':cities_names,'final_path':FINAL_DIR})


#View For SignUp Page
class SignUpView(View):

  def get(self,request,*args,**kwargs):
    return render(request,'mysite/sign-up.html',context={})


class CityView(ListView):
  model=Hotel
  template_name='mysite/hotels.html'
  def get(self,request,*args,**kwargs):
    hotel_data=self.get_queryset()
    return render(request,'mysite/hotels.html',context={'title':self.kwargs['city'],'hotel_data':hotel_data})
  def get_queryset(self,*args,**kwargs):
    context_object=Hotel.objects.filter(city=self.kwargs['city'])
    return context_object

class HotelView(ListView):
  model=Hotel
  template_name='mysite/hotel.html'
  def get(self,request,*args,**kwargs):
    hotel=self.get_queryset()
    rooms=hotel.hotel_rooms()
    return render(request,'mysite/hotel.html',context={'hotel':hotel,'rooms':rooms})
  def get_queryset(self):
    print(self.kwargs['id'])
    context_object=Hotel.objects.get(id=self.kwargs['id'])
    return context_object


class RoomView(View):
  model=Room
  template_name='mysite/room.html'
  def get(self,request,*args,**kwargs):
    context_object=self.get_queryset()
    print(Room.objects.filter(type=context_object.type).filter(is_available=True))
    count=len(Room.objects.filter(type=context_object.type).filter(is_available=True))
    print(count)
    try:
      booking_data=Booking.objects.filter(user=request.user)
    except:
      return render(request,'mysite/room.html',context={'room':context_object,'bookings':None,'available_count':count})
    else:
      return render(request,'mysite/room.html',context={'room':context_object,'bookings':booking_data,'available_count':count})     
  def get_queryset(self):
    context_object=Room.objects.get(id=self.kwargs['room'])
    return context_object
  def post(self,request,*args,**kwargs):
    user=User.objects.get(email=request.user)
    hotel=Hotel.objects.get(id=self.kwargs['hotel'])
    count=request.POST.get('quantity')
    bookings=[]
    for x in range(int(count)):
      room=Room.objects.filter(type=request.POST.get("type")).filter(is_available=True)[x]
      print(room)
      bookings.append(Booking(user=user,room=room,hotel=hotel,nights=request.POST.get('night')))
      bookings[x].save()
    return HttpResponse('')


class MyBookings(ListView):
  model=Booking
  template_name="mysite/my-bookings.html"


############################# (Functions Views) ######################

@login_required
def logout_view(request,*args,**kwargs):
  logout(request)
  return redirect(reverse('mysite:home'))

