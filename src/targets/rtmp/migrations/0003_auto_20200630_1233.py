# Generated by Django 3.0.7 on 2020-06-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtmp', '0002_auto_20200630_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtmp',
            name='destination_password',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='rtmp',
            name='destination_username',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
