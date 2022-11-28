from django.urls import re_path as url
from django.urls import path, include
from .api import RegisterApi
from rest_framework import routers
from .views import ServiceRequestViewset

router = routers.DefaultRouter()
router.register(r'service_requests', ServiceRequestViewset)
urlpatterns = [
      path('', include(router.urls)),
      path('api/register', RegisterApi.as_view()),
      
]