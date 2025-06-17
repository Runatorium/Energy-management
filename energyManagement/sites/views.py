from django.shortcuts import render
from .serializers import SiteSerializer,TechnicianSerializer
from .models import Site,Technician
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from energyManagement.permissions import IsAllowedTechnicianOrReadOnly




#Service for Creating new Sites, this ideally should be be done with it's own comprehensive system as i assume
#that the creation of any new site would not be entrusted to either a technician or a common user
#keeping this in mind i provide the ability to create/manage Sites to superusers only

class SiteListCreateView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminUser]

class SiteDestroyView(generics.DestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminUser]

class SiteUpdateView(generics.UpdateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminUser]

#Sites remain available for viewing by all technicians assigned to them
class SiteDetailView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAllowedTechnicianOrReadOnly]


#Techicians follows the same logic as Sites, they are not to be created by common users
class TechnicianListCreateView(generics.ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = [IsAdminUser]
    
class TechnicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = [IsAdminUser]