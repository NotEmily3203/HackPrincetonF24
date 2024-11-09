from django.db import models

# Create your models here.
class UserInfo(models.Model):  # Inherit from models.Model
    owner = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
