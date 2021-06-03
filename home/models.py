from django.db import models


# Create your models here.

class UserName(models.Model):
    Name = models.CharField(max_length=100)
