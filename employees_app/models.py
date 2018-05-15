from django.db import models
import os
from datetime import datetime
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Employees(models.Model):

    STATE = (
        ('ON', 'ON'),
    )

    POSITION = (
        ('Estimator', 'Estimator'),
        ('IT', 'IT'),
        ('Labour', 'Labour'),
        ('Manager', 'Manager'),
        ('Office_Staff', 'Office_Staff'),
        ('Shingler', 'Shingler'),
    )

    STATUS = (
        ('Citizen', 'Citizen'),
        ('Permanent_Resident', 'Permanent_Resident'),
        ('Refugee', 'Refugee'),
        ('Working_Visa', 'Working_Visa'),
        ('NONE', 'NONE'),
    )

    CLOTHES_SIZE = (
        ('2XL', '2XL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS', 'XS'),
    )

    WHMIS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    WRK_HEIGHTS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    WRK_HLTH_SFTY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    PROP_CONSTR = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=128)
    state = models.CharField(max_length=2, choices=STATE, default="")
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=90, default="Toronto")
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=16)

    # Work since - until:
    employed_from = models.DateField(default=datetime.now)
    employed_until = models.DateField(blank=True, null=True)

    sin = models.CharField(max_length=12, blank=True, null=True)
    position = models.CharField(max_length=25, choices=POSITION, default="")
    wage = models.CharField(max_length=12)
    driver_lic = models.CharField(max_length=12, blank=True, null=True)
    wsib = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=18, choices=STATUS, default="")
    clothes_size = models.CharField(max_length=3, choices=CLOTHES_SIZE, default="")
    whmis = models.CharField(max_length=3, choices=WHMIS, default="")
    work_heights = models.CharField(max_length=3, choices=WRK_HEIGHTS, default="")
    worker_health_safety = models.CharField(max_length=3, choices=WRK_HLTH_SFTY, default="")
    propane_in_construction = models.CharField(max_length=3, choices=PROP_CONSTR, default="")
    note = models.TextField(blank=True, null=True)
    # Images:
    # img_sin = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    # img_driver_lic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    # img_contract = models.ImageField(upload_to=get_image_path, blank=True, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
