# Generated by Django 5.1.7 on 2025-03-24 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_system', '0002_shipment_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='route',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
