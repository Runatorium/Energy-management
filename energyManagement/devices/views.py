from django.shortcuts import render
from .serializers import DeviceMetricSerializer,DeviceSerializer,MetricsSubcriptionSerializer
from .models import Device,DeviceMetric,MetricsSubcription
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser
from energyManagement.permissions import IsAllowedTechnicianOrReadOnly
from django.db.models import OuterRef, Subquery
from datetime import datetime

def get_queryset(self):
    qs = MetricsSubcription.objects.all()
    start_str = self.request.query_params.get("start")
    end_str   = self.request.query_params.get("end")

    if start_str and end_str:
        try:
            start = datetime.fromisoformat(start_str.replace("Z", "+00:00"))
            end   = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            return qs.filter(created_on__range=(start, end))
        except ValueError:
            return MetricsSubcription.objects.none()

    return qs
# Create your views here.
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedTechnicianOrReadOnly]

class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedTechnicianOrReadOnly]
    #here the latest metric for each device is annotated to the queryset
    def get_queryset(self):
        latest_metric = DeviceMetric.objects.filter(device=OuterRef('pk')).order_by('-created_on')
        latest_metric_value = {
            "value":Subquery(latest_metric.values('value')[:1]),
            "unit":Subquery(latest_metric.values('unit')[:1]),
            "timestamp":Subquery(latest_metric.values('created_on')[:1])
        }
        return Device.objects.annotate(**latest_metric_value)
        

class DeviceMetricListCreateView(generics.ListCreateAPIView):
    queryset = DeviceMetric.objects.all()
    serializer_class = DeviceMetricSerializer
    permission_classes = [permissions.IsAuthenticated,IsAllowedTechnicianOrReadOnly]

#the ability to update or delete a metric is not provided, as it is assumed that metrics are immutable once created
#they can still be viewed by anyone authenticated
class DeviceMetricDetailView(generics.RetrieveAPIView):
    queryset = DeviceMetric.objects.all()
    serializer_class = DeviceMetricSerializer
    permission_classes = [permissions.IsAuthenticated]



#every authenticated user can create a metrics subscription
class MetricsSubcriptionListCreateView(generics.ListCreateAPIView):
    queryset = MetricsSubcription.objects.all()
    serializer_class = MetricsSubcriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    #auto assign the user who created the subscription
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MetricsSubcriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetricsSubcription.objects.all()
    serializer_class = MetricsSubcriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class MetricsSubcriptionFilteredListView(generics.ListAPIView):
    serializer_class = MetricsSubcriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    #site insensitive as i am not sure if that is a requirement or not
    def get_queryset(self):
        qs = MetricsSubcription.objects.all()
        start_str = self.request.query_params.get("start")
        end_str = self.request.query_params.get("end")

        if start_str and end_str:
            try:
                start = datetime.fromisoformat(start_str.replace("Z", "+00:00"))
                end = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
                return qs.filter(created_on__range=(start, end))
            except ValueError:
                return MetricsSubcription.objects.none()

        return qs
