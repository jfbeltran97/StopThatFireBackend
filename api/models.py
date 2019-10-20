from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15)


class Location(models.Model):
    lng = models.DecimalField(max_digits=12, decimal_places=9)
    lat = models.DecimalField(max_digits=12, decimal_places=9)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
