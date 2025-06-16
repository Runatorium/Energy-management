from django.contrib import admin
from .models import Device,DeviceMetric,MetricsSubcription

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'site', 'name']
    search_fields = ['site', 'name'] 

@admin.register(DeviceMetric)
class DeviceMetricAdmin(admin.ModelAdmin):
    list_display = ['id', 'site', 'device', 'value', 'unit', 'created_by', 'created_on']
    search_fields = ['site__name', 'device__name', 'value', 'unit']

@admin.register(MetricsSubcription)
class MetricsSubcriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'created_on']
    search_fields = ['created_by__username', 'created_on']
