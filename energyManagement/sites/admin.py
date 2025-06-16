from django.contrib import admin
from .models import Site, Technician



@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = ['name', 'email']

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']
    search_fields = ['name', 'location']    