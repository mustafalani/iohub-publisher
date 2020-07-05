from django.db import models
from django.utils.timezone import now
from applications.models import Application
# Create your models here.
class FACEBOOK(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name        = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    source_stream_name = models.CharField(max_length=512)
    destination_application_name = models.CharField(max_length=512)
    destination_host = models.CharField(max_length=512)
    destination_port = models.IntegerField()
    destination_stream_name = models.CharField(max_length=512)
    shares = (("TIMELINE", "Time Line"), ("PAGE", "Page"))
    sharedon = models.CharField(max_length=9, choices=shares,default="TIMELINE")
    privacies = (
            ("ONLYME", "Only Me"), ("FRIENDS", "Friends"), ("FRIENDSOFFRIENDS", "Friends of Friends"),
            ("PUBLIC", "Public"))
    privacy =  models.CharField(max_length=128, choices=privacies,default="ONLYME")
    facebook_title = models.CharField(blank=True,null=True, max_length=512)
    facebook_description = models.TextField(blank=True, null=True)
    send_continuous_live = models.BooleanField(default=False)
    enable_schedule = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=now, blank=True)
    end_time = models.DateTimeField(default=now, blank=True)