from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Site,Technician



class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class SiteSerializer(serializers.ModelSerializer):
    technicians = serializers.PrimaryKeyRelatedField(
        many=True,                              
        queryset=Technician.objects.all()
    )
    class Meta:
        model = Site
        fields = "__all__"
    # here i could add a series of validators based on custom need,
    # im not gonna write extensive validation for this project
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Site name must be at least 3 characters long.")
        return value
