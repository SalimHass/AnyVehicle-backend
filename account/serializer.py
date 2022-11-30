from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ServiceRequest


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                                        email=validated_data['email'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ServiceRequestSerializer(serializers.ModelSerializer):
    service_status_display = serializers.CharField(source='get_service_status_display',read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    display_date = serializers.DateTimeField(source='date', format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class UserServiceRequestSerializer(serializers.ModelSerializer):
    service_status_display = serializers.CharField(source='get_service_status_display', read_only=True)
    display_date = serializers.DateTimeField(source='date', format="%Y-%m-%d %H:%M", read_only=True)
    
    class Meta:
        model = ServiceRequest
        fields = '__all__'
