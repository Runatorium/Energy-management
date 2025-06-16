from rest_framework import permissions
from sites.models import Technician
from devices.models import Device
class IsAllowedTechnicianOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            site_id = request.data.get('site')
            if not site_id:
                return False
            try:
                technician = Technician.objects.get(user=request.user)
                return technician.site_set.filter(id=site_id).exists()
            except Technician.DoesNotExist:
                return False

        return True 
    
    def has_object_permission(self, request, view, obj: Device):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            technician = Technician.objects.get(user=request.user)
            return obj.site.technicians.filter(id=technician.id).exists()
        except Technician.DoesNotExist:
            return False