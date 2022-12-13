
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views,login,authenticate,logout
from django.views.generic import TemplateView,View
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User

# Create your views here.

####################  (Class Views) ######################
##Login View
class LoginView(views.LoginView):
  # success_url=reverse_lazy('mysite:home')
  def post(self, request, *args: str, **kwargs):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request=request,username=username,password=password)
    try:
      user2=User.objects.get(username=username)
      print(user2)
      return render(request,'registration/login.html',context={'password':'• Incorrect Password'})
    except:
      if user is not None:
        login(request=request,user=user)
        return redirect(reverse('mysite:home'))
      else:
        return render(request,'registration/login.html',context={'data':'• User does not exist'})
  
  def get(self, request, *args: str, **kwargs):
    print("Came2")
    return render(request,'registration/login.html',context={})

class HomeView(TemplateView):
  template_name='home.html'

class SignUpView(View):
  def get(self,request,*args,**kwargs):
    return render(request,'mysite/sign-up.html',context={})


############################# (Functions Views) ######################


def logout_view(request,*args,**kwargs):
  logout(request)
  return redirect(reverse('mysite:home'))

