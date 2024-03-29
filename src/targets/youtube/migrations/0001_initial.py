# Generated by Django 3.0.7 on 2020-06-30 22:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0004_auto_20200629_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_stream_name', models.CharField(max_length=512)),
                ('destination_application_name', models.CharField(max_length=512)),
                ('destination_host', models.CharField(max_length=512)),
                ('destination_port', models.IntegerField()),
                ('destination_stream_name', models.CharField(max_length=512)),
                ('sharedon', models.CharField(choices=[('TIMELINE', 'Time Line'), ('PAGE', 'Page')], default='TIMELINE', max_length=9)),
                ('privacy_status', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('UNLISTED', 'Unlisted')], default='PUBLIC', max_length=128)),
                ('youtube_title', models.CharField(blank=True, max_length=512, null=True)),
                ('youtube_description', models.TextField(blank=True, null=True)),
                ('enable_schedule', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Application')),
            ],
        ),
    ]
