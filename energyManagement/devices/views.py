from django.shortcuts import render
from .serializers import DeviceMetricSerializer,DeviceSerializer,MetricsSubcriptionSerializer
from .models import Device,DeviceMetric,MetricsSubcription
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from energyManagement.permissions import IsAllowedTechnicianOrReadOnly

# Create your views here.
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated,IsAllowedTechnicianOrReadOnly]

class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated,IsAllowedTechnicianOrReadOnly]