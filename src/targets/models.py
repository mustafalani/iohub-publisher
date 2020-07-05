from django.db import models
from applications.models import Application
# Create your models here.
class Target(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name        = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)