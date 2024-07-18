from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal

class Drone(models.Model):
    BRAND_CHOICES = [
        ('DJI', 'DJI'),
        ('Parrot', 'Parrot'),
        ('Yuneec', 'Yuneec'),
        ('Autel', 'Autel'),
    ]
    
    CATEGORY_CHOICES = [
        ('Consumer', 'Consumer'),
        ('Professional', 'Professional'),
        ('Racing', 'Racing'),
    ]

    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.brand} {self.model}"

class Rental(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.drone} rented by {self.user}"
    
    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.drone.availability = False
            duration = self.end_time - self.start_time
            hours = Decimal(duration.total_seconds()) / Decimal(3600)
            self.total_price = Decimal(hours) * Decimal(self.drone.price_per_hour)
            self.drone.save()
        super().save(*args, **kwargs)