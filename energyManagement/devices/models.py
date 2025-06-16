from django.db import models
from sites.models import Site 
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Device(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)


class DeviceMetric(models.Model):
    site =  models.ForeignKey(Site, on_delete=models.CASCADE,null=False,blank=False)  #i assume that metrics are site specific
    device = models.ForeignKey(Device, on_delete=models.CASCADE,null=False,blank=False)
    value = models.CharField(max_length=100,null=False,blank=False)                           #i assume data could be something other then a number
    unit = models.CharField(max_length=100,null=False,blank=False)                            #i assume unit of measure can be various and are most likely not covered by django-measurament
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    created_on = models.DateTimeField(default=timezone.now,null=False,blank=False)


class MetricsSubcription(models.Model):
    deviceMetrics = models.ManyToManyField(DeviceMetric)
    sites = models.ManyToManyField(Site)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    created_on = models.DateTimeField(default=timezone.now,null=False,blank=False)