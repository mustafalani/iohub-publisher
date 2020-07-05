from django.db import models

# serializers.py
from rest_framework import serializers

from applications.models import Application

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'description', 'type')