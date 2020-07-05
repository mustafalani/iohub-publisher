from django.db import models
from django.utils.timezone import now
from applications.models import Application
# Create your models here.
class YouTube(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name        = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    source_stream_name = models.CharField(max_length=512)
    destination_application_name = models.CharField(max_length=512)
    destination_host = models.CharField(max_length=512)
    destination_port = models.IntegerField()
    destination_stream_name = models.CharField(max_length=512)
    privacies = (
            ("PRIVATE", "Private"), ("PUBLIC", "Public"), ("UNLISTED", "Unlisted"))
    privacy_status =  models.CharField(max_length=128, choices=privacies,default="PUBLIC")
    youtube_title = models.CharField(blank=True,null=True, max_length=512)
    youtube_description = models.TextField(blank=True, null=True)
    enable_schedule = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=now, blank=True)
    end_time = models.DateTimeField(default=now, blank=True)