import requests
from config import Config

async def get_rapido_fare(pickup, dropoff):
    response = [
        {'vehicleType': 'Auto-Rickshaw', 'fare': 75},
        {'vehicleType': 'Bike Taxi', 'fare': 45},
    ]
    return [{'vehicleType': item['vehicleType'], 'fare': item['fare'], 'provider': 'Rapido'} for item in response]