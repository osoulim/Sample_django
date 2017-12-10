from django.db import models

# Create your models here.

class VisitTime(models.Model):
    time = models.CharField(max_length=100)

