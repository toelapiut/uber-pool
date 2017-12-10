from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Q, signals
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from uber import settings
# Create your models here.

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='user_pics/', blank=True)
    car_picture = models.ImageField(upload_to='user_pics/')
    number_plates = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    vehicle_name = models.CharField(max_length=60)
    vehicle_model = models.CharField(max_length=60)
    bio = models.CharField(max_length=140, blank=True)



User.profile = property(
    lambda u: Driver.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Driver.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)

# Create your Rider models here.

class Rider(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rider_profile', unique=True)
    picture = models.ImageField(upload_to='user_pics/', blank=True)
    phone =models.CharField(max_length=30)
    bio = models.CharField(max_length=500, blank=True)
    username=models.CharField(max_length=12,blank=True)
    email=models.EmailField()

    @staticmethod
    def default_riders_group(sender, instance, created, **kwargs):
        if created and settings.REGISTRATION_DEFAULT_GROUP_NAME:
            instance.groups.add(Group.objects.get(
                name=settings.REGISTRATION_DEFAULT_GROUP_NAME))

    @staticmethod
    def is_rider(instance):
        return instance.groups.filter(name='riders').exists()


post_save.connect(Rider.default_riders_group, sender=User)


User.rider_profile = property(
    lambda u: Rider.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Rider.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.rider_profile.save()


post_save.connect(create_user_profile, sender=User)

class Driver_Or_Rider(models.Model):  

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    selection=models.IntegerField()
