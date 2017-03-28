from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sensor(models.Model):#Stores information about sensor values
    Sensor_name      = models.CharField(max_length=200,default=None)
    Sensor_value        = models.CharField(max_length=200,default=None)
    def __str__(self):
        return '@'+self.Sensor_name
      
