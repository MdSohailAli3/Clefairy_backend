from urllib import response

from fastapi import APIRouter, HTTPException
from app.schemas.route_schema import RouteRequest, RouteResponseItem, RouteResponse
from app.services.risk_service import rank_routes
from app.services.directions_service import fetch_routes
from app.services.polyline_service import decode_route_polyline
from app.models.route_model import Route as MLRoute
from app.schemas.route_schema import Coordinate as CoordinateSchema

router = APIRouter(prefix="/users/routes", tags=["Route Risk"])


@router.post("/safe-route", response_model=RouteResponse)
async def get_safe_route(data: RouteRequest):
    """
    1. Fetch routes from Google Directions API
    2. Decode polylines into coordinates
    3. Run ML risk ranking
    4. Return safest route
    """

    # ---------- Fetch routes ----------
    routes = await fetch_routes(
        origin=(data.origin_lat, data.origin_lng),
        destination=(data.dest_lat, data.dest_lng)
    )
    # demo response
    # routes = [
        #     {
        #         "distanceMeters": 1240,
        #         "duration": "980s",
        #         "polyline": {
        #             "encodedPolyline": "u{~vFvyys@..."
        #         }
        #     }
        # ]

    if not routes:
        raise HTTPException(
            status_code=404,
            detail="No routes found"
        )

    # ---------- Convert polylines ----------
    processed_routes = []
    route_metadata = []

    for idx, route in enumerate(routes):
        coords = decode_route_polyline(route)
        duration_sec = int(route["duration"].replace("s",""))
        # [Coordinate, Coordinate, Coordinate] objects of coordinate class
        processed_routes.append(
            MLRoute(coordinates=coords)
        )

        route_metadata.append({
            "route_index": idx,
            "distance": route["distanceMeters"],
            "duration": duration_sec,
            "coordinates": coords
            })
# processed_rout =
#          [
        #     Route(
        #         coordinates=[
        #             Coordinate(28.6139, 77.2090),
        #             Coordinate(28.6141, 77.2093),
        #             Coordinate(28.6145, 77.2098)
        #         ]
        #     ),

        #     Route(
        #         coordinates=[
        #             Coordinate(28.6138, 77.2085),
        #             Coordinate(28.6140, 77.2091),
        #             Coordinate(28.6147, 77.2102)
        #         ]
        #     )
        # ]


    # ---------- ML ranking ----------
    safest_route = rank_routes(processed_routes)

    response_routes = [
        RouteResponseItem(
            route_index=meta["route_index"],
            coordinates=[
                CoordinateSchema(lat=c.lat, lng=c.lng)  # ✅ convert manually
                for c in meta["coordinates"]
            ],
            distance=meta["distance"],
            duration=meta["duration"]
        )
        for meta in route_metadata
    ]

    
    # ---------- Response ----------
    return RouteResponse(
        routes=response_routes,
        safest_route_index=safest_route.index
    )
