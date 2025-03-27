"""
URL configuration for tracking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# tracking_system/urls.py
# tracking_system/urls.py
# tracking_system/urls.py
from django.urls import path
from .views import home, track_shipment  # Ensure views.py has these functions

urlpatterns = [
    path('', home, name='home'),  
    path('track_shipment/<str:tracking_id>/', track_shipment, name='track_shipment'),  
]




