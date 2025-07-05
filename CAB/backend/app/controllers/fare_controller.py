from flask import jsonify
from datetime import datetime, timedelta
from ..models.fare_estimate import FareEstimate
from ..services.ola_service import get_ola_fare
from ..services.uber_service import get_uber_fare
from ..services.rapido_service import get_rapido_fare
from ..services.google_maps_service import geocode_address
import asyncio

async def compare_fares(pickup_address, dropoff_address):
    try:
        pickup = await geocode_address(pickup_address)
        dropoff = await geocode_address(dropoff_address)

        cached_fares = list(FareEstimate.find_recent(pickup, dropoff))
        if cached_fares:
            return jsonify(aggregate_fares(cached_fares))

        ola_fares, uber_fares, rapido_fares = await asyncio.gather(
            get_ola_fare(pickup, dropoff),
            get_uber_fare(pickup, dropoff),
            get_rapido_fare(pickup, dropoff)
        )
        all_fares = ola_fares + uber_fares + rapido_fares

        if all_fares:
            FareEstimate.insert_many([
                {
                    'pickup': pickup,
                    'dropoff': dropoff,
                    'vehicleType': fare['vehicleType'],
                    'provider': fare['provider'],
                    'fare': fare['fare'],
                    'timestamp': datetime.utcnow()
                } for fare in all_fares
            ])

        return jsonify(aggregate_fares(all_fares))
    except Exception as e:
        return jsonify({'error': 'Failed to compare fares'}), 500

def aggregate_fares(fares):
    vehicle_types = list(set(f['vehicleType'] for f in fares))
    return [
        {
            'vehicleType': vehicle_type,
            'cheapestFare': min(
                (f['fare'] for f in fares if f['vehicleType'] == vehicle_type),
                default=None
            ),
            'provider': next(
                (f['provider'] for f in fares if f['vehicleType'] == vehicle_type and f['fare'] == min(
                    (f['fare'] for f in fares if f['vehicleType'] == vehicle_type),
                    default=None
                )),
                None
            )
        }
        for vehicle_type in vehicle_types
    ]