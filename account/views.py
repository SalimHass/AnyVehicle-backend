from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import ServiceRequest
from .serializer import ServiceRequestSerializer, UserServiceRequestSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_service_requests(request):
    if request.user.is_superuser:
        request_list = ServiceRequest.objects.all()
        return Response(ServiceRequestSerializer(request_list, many=True).data)
    else:
        user_id = request.user.id
        request_list = ServiceRequest.objects.filter(user_id=user_id)
        return Response(UserServiceRequestSerializer(request_list, many=True).data)


