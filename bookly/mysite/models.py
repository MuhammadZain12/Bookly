from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.




class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError('Email required')
      
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,name,cnic,age,gender=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not name:
            raise ValueError('Name required')
        if not cnic:
            raise ValueError('Cnic required')     
        return self._create_user(email,password, {'name':name,'cnic':cnic,'age':age})

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be a superuser'
            )

        return self._create_user(email, password, **extra_fields)



# User Model That We Used In Our Project
class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    email = models.EmailField('email',unique=True,max_length=255,blank=False)
    name = models.CharField('name',max_length=150,blank=False)
    cnic= models.PositiveBigIntegerField(unique=True,null=True,blank=False)
    age=models.SmallIntegerField(null=True,blank=False)
    # gender=models.BooleanField(null=True,blank=True)
    is_verified=models.BooleanField('verified',default=False)
    is_staff = models.BooleanField('staff status',default=False)
    is_active = models.BooleanField('active',default=False)
    is_superuser = models.BooleanField('superuser',default=False)
    date_joined = models.DateTimeField('date joined',default=timezone.now)
     
    REQUIRED_FIELDS=[]
    objects = UserManager()

    def verify_user(self):
        self.is_verified=True


    def __str__(self):
        return self.email


#Hotels model

class Hotel(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=6,)
    name=models.CharField(max_length=25,blank=False)
    small_description=models.TextField(default=name)
    description=models.TextField(default=name)
    city=models.CharField(max_length=20)
    image1=models.ImageField(upload_to='static/mysite/hotels',blank=True)
    image2=models.ImageField(upload_to='static/mysite/hotels',blank=True)
    image3=models.ImageField(upload_to='static/mysite/hotels',blank=True)
    image4=models.ImageField(upload_to='static/mysite/hotels',blank=True)
    image5=models.ImageField(upload_to='static/mysite/hotels',blank=True)
    # hotel_image2=models.ImageField()
    
    def hotel_rooms(self):
      return self.rooms.all()


    def __str__(self) -> str:
        return f"{self.id} {self.name}"


class Room(models.Model):
    hotel=models.ForeignKey('mysite.Hotel',related_name='rooms',on_delete=models.CASCADE)
    id=models.CharField(primary_key=True,unique=True,max_length=6)
    type=models.CharField(max_length=20)
    small_description=models.TextField(default=type)
    description=models.TextField(default=type)
    facilities=models.TextField(default="Lorum Ipsum")
    capacity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='static/mysite/rooms',blank=True)
    is_available=models.BooleanField('available',default=True)
    
    def save(self,*args,**kwargs):
        if len(self.id)<4:
            id=self.id
            self.id=f"{self.hotel.id}{id}"
        return super().save(*args,**kwargs)
    def get_hotid(self):
        return self.hotel.id
    def isBooked(self,signal):
        if signal:
            self.is_available=False
        else:
            self.is_available=True    
    def __str__(self) -> str:
        return f"{self.id} {self.type}"
      


class Booking(models.Model):
    user=models.ForeignKey('mysite.User',related_name='bookings',on_delete=models.CASCADE)
    hotel=models.ForeignKey('mysite.Hotel',related_name='bookings',on_delete=models.CASCADE)
    room=models.ForeignKey('mysite.Room',related_name='booking',on_delete=models.CASCADE)
    nights=models.IntegerField()
    id=models.CharField(primary_key=True,max_length=50)
    is_verified=models.BooleanField('verified',default=False)

    def save(self,*args,**kwargs):
        self.id=self.hotel.id+self.room.id+self.user.email
        if self.is_verified:
            self.room.is_available=False
        else:
            self.room.is_available=True 
        self.room.save()   
        return super().save(*args,**kwargs)    
    
    def __str__(self) -> str:
        return f"{self.id}"

