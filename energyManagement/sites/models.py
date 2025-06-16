from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings



class Site(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    location = models.CharField(max_length=100,blank=False,null=False)
    technicians = models.ManyToManyField('Technician')


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)




