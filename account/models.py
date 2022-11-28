from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ServiceStatus(models.IntegerChoices):
    accepted = 0, 'Accepted'
    pending = 1, 'Pending'
    dismissed=2, 'Dismissed'
    completed=3, 'Completed'

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_request=models.CharField(max_length=250)
    service_status= models.IntegerField(default=ServiceStatus.pending, choices=ServiceStatus.choices)
    date=models.DateTimeField(auto_now=True)



