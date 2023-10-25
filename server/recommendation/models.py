from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=255)
    ph = models.DecimalField(max_digits=3, decimal_places=1)
    nitrogen = models.DecimalField(max_digits=5, decimal_places=2)
    potassium = models.DecimalField(max_digits=5, decimal_places=2)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    soil_type = models.CharField(max_length=100)
