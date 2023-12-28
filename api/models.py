from django.db import models

# Create your models here.
class Riddle(models.Model):
    question = models.CharField(max_length=255, unique=True, blank=False, null=False)
    answer = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    enable = models.BooleanField(default=False)