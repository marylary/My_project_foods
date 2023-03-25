from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    tel_num = models.CharField(max_length=200, blank=True)

class Person(models.Model):
    username = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    password1 = models.CharField(max_length=10, blank=True)
    password2 = models.CharField(max_length=10, blank=True)

