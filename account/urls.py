from django.urls import re_path as url
from django.urls import path, include
from .api import RegisterApi
from rest_framework import routers
from .views import ServiceRequestViewSet, get_user_service_requests

router = routers.DefaultRouter()
router.register(r'service_requests', ServiceRequestViewSet)
urlpatterns = [
      path('', include(router.urls)),
      path('register/', RegisterApi.as_view()),
      path('user_services/', get_user_service_requests, name='get_user_service_requests'),
      
]