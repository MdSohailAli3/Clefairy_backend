from app.services.sampling_service import prepare_route_points
from app.ml_models.ml_model import predict_route_risk
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
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
def rank_routes(routes): # list of routes

    for i, route in enumerate(routes):

        # ---------- sampling ----------
        sampled_points = prepare_route_points(route.coordinates)

        # shape → (num_points, 2)
        # np array (list of list of lat and long)

        # ---------- predict risk per point ----------
        point_risks = predict_route_risk(sampled_points)

        # ---------- aggregate route risk ----------
        route_risk = float(np.mean(point_risks))
        print(f"Route {i} Point Risks: {point_risks}")
        route.risk_score = route_risk
        route.index = i

    # ---------- safest route ----------
    safest_route = min(routes, key=lambda x: x.risk_score)

    return safest_route 