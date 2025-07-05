# Mobility Control Plane

A system to compare fares from Ola, Uber, and Rapido for different vehicle types using Flask backend and React frontend.

## Setup

### Backend
1. Navigate to `backend/`.
2. Install Python 3.8+ and pip.
3. Install dependencies: `pip install -r requirements.txt`.
4. Set up environment variables in `backend/.env` (MongoDB URI, API keys).
5. Start the server: `python run.py`.

### Frontend
1. Navigate to `frontend/`.
2. Install Node.js and npm.
3. Install dependencies: `npm install`.
4. Start the development server: `npm start`.

## Usage
1. Open the frontend in a browser (e.g., `http://localhost:3000`).
2. Enter pickup and drop-off addresses.
3. View the cheapest fares per vehicle type.

## Notes
- Replace simulated API calls in `ola_service.py`, `uber_service.py`, and `rapido_service.py` with real API endpoints.
- Obtain API keys from Ola, Uber, Rapido, and Google Maps.
- MongoDB is used for caching; ensure it's running locally or use a cloud instance.
- The backend uses Flask with async support for API calls.