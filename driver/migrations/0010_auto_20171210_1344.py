# Generated by Django 2.0 on 2017-12-10 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0009_driver_or_rider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver_or_rider',
            old_name='user_id',
            new_name='user',
        ),
    ]
