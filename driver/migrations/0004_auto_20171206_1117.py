# Generated by Django 2.0 on 2017-12-06 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_auto_20171205_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='vehicle_model',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
