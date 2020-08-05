from django.db import models
from django.utils.timezone import now
from applications.models import Application
# python
import os, configparser, subprocess, json
from pathlib import Path
from shutil import copyfile

# Create your models here.
class RTMP(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name        = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    source_stream_name = models.CharField(max_length=512)
    destination_application_name = models.CharField(max_length=512)
    destination_host = models.CharField(max_length=512)
    destination_port = models.IntegerField()
    destination_stream_name = models.CharField(max_length=512)
    destination_username = models.CharField(blank=True,null=True, max_length=512)
    destination_password = models.CharField(blank=True,null=True, max_length=512)
    enable_schedule = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=now, blank=True)
    end_time = models.DateTimeField(default=now, blank=True)
    dirname = os.path.dirname(__file__)
    if not os.path.isdir(dirname + 'rtmpconf'):
        os.makedirs(dirname + 'rtmpconf')
    copyfile(dirname + '/rtmp.conf',dirname + '/Application.conf')