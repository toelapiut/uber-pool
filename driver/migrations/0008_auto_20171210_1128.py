# Generated by Django 2.0 on 2017-12-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_driver_or_rider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver_or_rider',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='driver_or_rider',
        ),
    ]