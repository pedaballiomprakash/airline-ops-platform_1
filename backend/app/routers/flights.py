from fastapi import APIRouter

router = APIRouter()

# Sample flights data
SAMPLE_FLIGHTS = [
    {
        "flight_number": "AA100",
        "origin": "New York (JFK)",
        "destination": "Los Angeles (LAX)",
        "status": "On Time"
    },
    {
        "flight_number": "UA205",
        "origin": "San Francisco (SFO)",
        "destination": "Chicago (ORD)",
        "status": "Delayed"
    },
    {
        "flight_number": "DL350",
        "origin": "Atlanta (ATL)",
        "destination": "Miami (MIA)",
        "status": "Boarding"
    }
]

@router.get("/api/flights")
def get_flights():
    return {"flights": SAMPLE_FLIGHTS}
