from django.contrib import admin
from tracking_system.models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'origin', 'destination', 'status')
