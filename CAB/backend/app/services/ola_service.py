import requests
from config import Config

async def get_ola_fare(pickup, dropoff):
    response = [
        {'vehicleType': 'Sedan', 'fare': 200},
        {'vehicleType': 'Auto-Rickshaw', 'fare': 80},
        {'vehicleType': 'Bike Taxi', 'fare': 50},
    ]
    return [{'vehicleType': item['vehicleType'], 'fare': item['fare'], 'provider': 'Ola'} for item in response]