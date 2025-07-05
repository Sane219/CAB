import requests
from config import Config

async def geocode_address(address):
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json',
        params={'address': address, 'key': Config.GOOGLE_MAPS_API_KEY}
    ).json()
    if response['status'] == 'OK':
        location = response['results'][0]['geometry']['location']
        return [location['lat'], location['lng']]
    raise Exception('Geocoding failed')