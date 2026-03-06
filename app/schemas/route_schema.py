from pydantic import BaseModel
from typing import List

class Coordinate(BaseModel):
    lat: float
    lng: float


class RouteResponseItem(BaseModel):
    coordinates: List[Coordinate]
    distance: float
    duration: float
    route_index: int  # added to explicitly share route index

class RouteRequest(BaseModel):
    origin_lat: float
    origin_lng: float
    dest_lat: float
    dest_lng: float


class RouteResponse(BaseModel):
    routes: List[RouteResponseItem]
    safest_route_index: int