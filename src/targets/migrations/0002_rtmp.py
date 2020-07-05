# Generated by Django 3.0.7 on 2020-06-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTMP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_stream_name', models.CharField(max_length=512)),
                ('destination_application_name', models.CharField(max_length=512)),
                ('destination_host', models.CharField(max_length=512)),
                ('destination_port', models.IntegerField()),
                ('destination_stream_name', models.CharField(max_length=512)),
                ('destination_username', models.CharField(blank=True, max_length=512, null=True)),
                ('destination_password', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]