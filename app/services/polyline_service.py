import polyline
from app.models.coordinate_model import Coordinate

# what it receive- demo
#               {
#                  "distanceMeters": 1240,
#                  "duration": "980s",
#                  "polyline": {
#                      "encodedPolyline": "u{~vFvyys@..."
#                  }
#              }

def decode_route_polyline(route):
    """
    Decode polyline from Google Routes API response.
    """

    try:
        encoded = route["polyline"]["encodedPolyline"]
    except KeyError:
        raise ValueError(
            f"Polyline not found in route response: {route}"
        )

    coords = polyline.decode(encoded) # [(latitude, longitude), (latitude, longitude), ...]

    return [ # [Coordinate, Coordinate, Coordinate]
        Coordinate(lat,lng)
        for lat, lng in coords
    ]