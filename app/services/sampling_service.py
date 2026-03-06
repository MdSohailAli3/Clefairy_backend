import numpy as np

def coords_to_numpy(coordinates):
    """
    Convert Coordinate objects → numpy array (N,2)
    """

    return np.array(
        [[p.lat, p.lng] for p in coordinates],
        dtype=float
    )


def sample_route_points(coords: np.ndarray, n_samples: int = 50):
    """
    Uniform sampling of route points.
    """

    if len(coords) == 0:
        raise ValueError("Empty coordinates")

    if len(coords) <= n_samples:
        return coords

    indices = np.linspace(
        0,
        len(coords) - 1,
        n_samples,
        dtype=int
    )

    return coords[indices]


def prepare_route_points(coordinates, n_samples=50):
    # coords = coords_to_numpy(coordinates) # list of coord objects
    return coords_to_numpy(coordinates) # list of coord objects

    # coords = np array of lat long
    # return sample_route_points(coords, n_samples)