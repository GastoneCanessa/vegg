from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    city=models.CharField(('city'), max_length=100, blank=True,null=True)
    address=models.CharField(('address'), max_length=100, blank=True,null=True)
    district=models.CharField(('district'), max_length=100, blank=True,null=True)
    postal_code=models.IntegerField(('CAP'), blank=True,null=True)
