from django.db import models


class VisitTime(models.Model):
    time = models.CharField(max_length=100)

