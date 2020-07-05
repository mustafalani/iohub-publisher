from django.db import models

# Create your models here.
class Application(models.Model):
    name        = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=True)
    types       = (("Live", "Live"),("VOD", "VOD"))
    type        = models.CharField(max_length=9,choices=types,default="Live")


