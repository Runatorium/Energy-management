from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Device,DeviceMetric,MetricsSubcription


class DeviceSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    class Meta:
        model = Device
        fields = "__all__"

class DeviceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceMetric
        fields = "__all__"

class MetricsSubcriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricsSubcription
        fields = "__all__"