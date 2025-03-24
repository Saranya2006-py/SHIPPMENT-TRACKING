from django.db import models

class Shipment(models.Model):
    tracking_id = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    ], default='Pending')

    def __str__(self):
        return self.tracking_id
