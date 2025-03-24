import math
from django.shortcuts import render
from django.http import JsonResponse
from .models import Shipment

# Haversine formula to calculate distance between two latitudes and longitudes
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Result in kilometers
    return distance

# Carbon emission calculation (simplified)
def calculate_carbon_emission(distance, transport_mode='road'):
    # Carbon emission factors (kg CO2 per km)
    emission_factors = {
        'road': 0.12,  # Example: 0.12 kg CO2 per km for road transport
        'air': 0.20,   # Example: 0.20 kg CO2 per km for air transport
        'sea': 0.05,   # Example: 0.05 kg CO2 per km for sea transport
    }
    
    emission_factor = emission_factors.get(transport_mode, 0.12)  # Default to 'road'
    carbon_emission = distance * emission_factor
    return carbon_emission

# Home page - Rendering index.html
def home(request):
    return render(request, "index.html")

# Shipment tracking API with carbon emission calculation
def track_shipment(request, tracking_id):
    try:
        shipment = Shipment.objects.get(tracking_id=tracking_id)

        # Ensure shipment has valid location data
        if shipment.latitude is None or shipment.longitude is None:
            return JsonResponse({"error": "Shipment location data missing"}, status=400)

        # Assuming we have the destination coordinates (lat, lon)
        destination_lat = 34.0522  # Example destination latitude (Los Angeles)
        destination_lon = -118.2437  # Example destination longitude

        # Get the current shipment coordinates (lat, lon)
        current_lat = shipment.latitude
        current_lon = shipment.longitude

        # Calculate the distance between current and destination coordinates
        distance = haversine(current_lat, current_lon, destination_lat, destination_lon)
        
        # Use shipment transport mode if available, otherwise default to 'road'
        transport_mode = getattr(shipment, "transport_mode", "road")
        carbon_emission = calculate_carbon_emission(distance, transport_mode)

        data = {
            "tracking_id": shipment.tracking_id,
            "status": shipment.status,
            "location": {
                "latitude": shipment.latitude,
                "longitude": shipment.longitude,
            },
            "carbon_emission": carbon_emission,  # Include carbon emission in the response
            "distance": distance,  # Include the calculated distance (in km)
        }

        return JsonResponse(data)

    except Shipment.DoesNotExist:
        return JsonResponse({"error": "Shipment not found"}, status=404)
