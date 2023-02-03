from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class auth_user_additional(models.Model):
    city = models.CharField(max_length=40, null=True, blank=True)
    coordinate = models.CharField(max_length=40, null=True, blank=True)
    IP = models.CharField(max_length=20, null=True, blank=True)
    lastpayment = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

