from django.db import models
from django.contrib.auth.models import User
import datetime


def current_year():
    return datetime.date.today().year


# Create your models here.

class ServiceStatus(models.IntegerChoices):
    accepted = 0, 'Accepted'
    pending = 1, 'Pending'
    dismissed = 2, 'Dismissed'
    completed = 3, 'Completed'


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_request = models.CharField(max_length=250)
    is_urgent = models.BooleanField(default=False)
    car_model = models.CharField(max_length=250)
    car_year = models.IntegerField(default=current_year)
    service_status = models.IntegerField(default=ServiceStatus.pending, choices=ServiceStatus.choices)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Service: " + self.service_request + " , Status: " + self.get_service_status_display() + \
               ", Urgent: " + str(self.is_urgent)
