# Generated by Django 3.0.7 on 2020-07-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20200629_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.CharField(choices=[('Live', 'Live'), ('VOD', 'VOD')], default='Live', max_length=9),
        ),
    ]
