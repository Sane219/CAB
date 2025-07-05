import requests
from config import Config

async def get_uber_fare(pickup, dropoff):
    response = [
        {'vehicleType': 'Sedan', 'fare': 220},
        {'vehicleType': 'Auto-Rickshaw', 'fare': 90},
        {'vehicleType': 'Bike Taxi', 'fare': 60},
        {'vehicleType': 'Premium', 'fare': 350},
    ]
    return [{'vehicleType': item['vehicleType'], 'fare': item['fare'], 'provider': 'Uber'} for item in response]