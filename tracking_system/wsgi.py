"""
WSGI config for tracking_system project.

This module contains the WSGI application used by Django’s development server
and any production WSGI deployments.

For more information, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'tracking_system' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracking_system.settings')

# Create the WSGI application
application = get_wsgi_application()
