from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Site,Technician

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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
