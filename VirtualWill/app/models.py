from django.db import models

# Create your models here.
class Creator(models.Model):  # Inherit from models.Model
    owner = models.CharField(max_length=100)
    owner_wallet = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    beneficiary_wallet = models.CharField(max_length=100)
    assets = models.CharField(max_length=100)

class Beneficiary(models.Model):  # Inherit from models.Model
    ifps_hash = models.CharField(max_length=100)

class Assignee(models.Model):  # Inherit from models.Model
    oracle = models.CharField(max_length=100)
