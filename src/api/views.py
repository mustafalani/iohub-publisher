from django.shortcuts import render

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import ApplicationSerializer
from applications.models import Application


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('id')
    serializer_class = ApplicationSerializer
    lookup_field = 'name'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']