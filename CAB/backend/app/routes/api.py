from flask import Blueprint, request
from ..controllers.fare_controller import compare_fares
import asyncio

api_bp = Blueprint('api', __name__)

@api_bp.route('/compare-fares', methods=['POST'])
async def compare_fares_route():
    data = request.get_json()
    pickup_address = data.get('pickupAddress')
    dropoff_address = data.get('dropoffAddress')
    if not pickup_address or not dropoff_address:
        return jsonify({'error': 'Missing pickup or dropoff address'}), 400
    return await compare_fares(pickup_address, dropoff_address)