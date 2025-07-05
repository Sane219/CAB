import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mobility_control_plane')
    OLA_API_KEY = os.getenv('OLA_API_KEY', 'your_ola_api_key')
    UBER_API_KEY = os.getenv('UBER_API_KEY', 'your_uber_api_key')
    RAPIDO_API_KEY = os.getenv('RAPIDO_API_KEY', 'your_rapido_api_key')
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', 'your_google_maps_api_key')