from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class Author(models.Model):
    fullname = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)    

class Book(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    authors = models.ManyToManyField(Author,related_name="authors")
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    categories = models.ManyToManyField(Category,related_name='books')
    rating = models.FloatField(null=True,blank=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    credit = models.FloatField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class History(models.Model):
    user = models.ForeignKey(CustomUser,related_name='user')
    query = models.TextField() 
    books = models.ManyToManyField(Book,related_name='books')


class Busket(models.Model):
    book = models.ManyToManyField(Book,related_name='books')    
    user = models.ForeignKey(CustomUser,related_name='user')

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser,related_name='user')   
    book = models.ForeignKey(Book)   
    number_books = models.IntegerField()