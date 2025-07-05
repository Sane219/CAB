from datetime import datetime
from .. import mongo

def create_fare_estimate_collection():
    # Create index for TTL (expire after 1 hour)
    mongo.db.fare_estimates.create_index("timestamp", expireAfterSeconds=3600)

class FareEstimate:
    @staticmethod
    def insert_many(fares):
        mongo.db.fare_estimates.insert_many(fares)
    
    @staticmethod
    def find_recent(pickup, dropoff):
        return mongo.db.fare_estimates.find({
            'pickup': pickup,
            'dropoff': dropoff,
            'timestamp': {'$gte': datetime.utcnow() - timedelta(minutes=30)}
        })