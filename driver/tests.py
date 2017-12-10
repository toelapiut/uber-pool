from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.


class DriverRiderTest(TestCase):
    def setUp(self):
        user=User.objects.get(id).all()
        self.driver_rider = Driver_Or_Rider(user_id=user, selection=1)

    # test for checking instance
    def test_isinstance(self):
        self.assertTrue(isinstance(self.driver_rider, Driver_Or_Rider))

    # test for saving
    def test_driver_rider_save(self):
        self.driver_rider.save_d_or_r()
        driver_riders = Driver_Or_Rider.objects.all()
        self.assertTrue(len(driver_rider) > 0)

    # test for deleting Driver or Editor
    def test_Driver_Rider_delete(self):
        self.driver_rider.save_d_or_r()()
        self.driver_rider.delete_d_or_r()()
        driver_riders = Driver_Or_Rider.objects.all()
        self.assertTrue(len(driver_riders) == 0)
