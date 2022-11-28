from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from .models import ServiceRequest
from .serializer import ServiceRequestSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.
class ServiceRequestViewset(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializers

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
