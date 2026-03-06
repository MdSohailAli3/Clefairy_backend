import httpx
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

ROUTES_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"


async def fetch_routes(origin, destination):
    """
    Calls Google Routes API (ComputeRoutes)
    and returns alternative routes.
    """

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_API_KEY,

        # VERY IMPORTANT → controls response size
        "X-Goog-FieldMask":
            "routes.polyline.encodedPolyline,"
            "routes.distanceMeters,"
            "routes.duration"
    }

    body = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin[0],
                    "longitude": origin[1]
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": destination[0],
                    "longitude": destination[1]
                }
            }
        },

        # multiple routes
        "computeAlternativeRoutes": True,

        "travelMode": "WALK",

        # best polyline quality for ML
        "polylineQuality": "HIGH_QUALITY"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            ROUTES_URL,
            headers=headers,
            json=body
        )

    data = response.json()

    if "routes" not in data:
        raise Exception(f"Routes API failed: {data}")

    return data["routes"]