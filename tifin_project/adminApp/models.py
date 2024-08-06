from django.db import models

# Create your models here.
class AdminModel (models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

