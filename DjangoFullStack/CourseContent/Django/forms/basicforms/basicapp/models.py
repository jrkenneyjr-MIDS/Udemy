from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    text = models.CharField(max_length = 60)
