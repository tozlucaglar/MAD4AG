#https://autogis-site.readthedocs.io/en/2019/notebooks/L3/nearest-neighbor-faster.html


from sklearn.neighbors import BallTree
import numpy as np


def get_nearest(src_points, candidates, k_neighbors=1):
    """Find nearest neighbors for all source points from a set of candidate points"""

    # Create tree from the candidate points
    tree = BallTree(candidates, leaf_size=10, metric='haversine')

    # Find closest points and distances
    distances, indices = tree.query(src_points, k=k_neighbors)

    # Transpose to get distances and indices into arrays
    distances = distances.transpose()
    indices = indices.transpose()

    # Get closest indices and distances (i.e. array at index 0)
    # note: for the second closest points, you would take index 1, etc.
    closest = indices[0]
    closest_dist = distances[0]

    # Return indices and distances
    return (closest, closest_dist)


def nearest_neighbor(left_gdf, right_gdf, return_dist=False):
    """
    For each point in left_gdf, find closest point in right GeoDataFrame and return them.

    NOTICE: Assumes that the input Points are in WGS84 projection (lat/lon).
    """

    #left_geom_col = left_gdf.geometry.name
    #right_geom_col = right_gdf.geometry.name

    # Ensure that index in right gdf is formed of sequential numbers
    right = right_gdf.copy().reset_index(drop=True)

    #convert degree to radian
    right['lat_rad'] = right.apply(lambda row: np.deg2rad(row['lat']), axis=1)
    right['lng_rad'] = right.apply(lambda row: np.deg2rad(row['lng']), axis=1)

    left_gdf['lat_rad'] = left_gdf.apply(lambda row: np.deg2rad(row['lat']), axis=1)
    left_gdf['lng_rad'] = left_gdf.apply(lambda row: np.deg2rad(row['lng']), axis=1)

    # Parse coordinates from points and insert them into a numpy array as RADIANS
    left_radians = np.array(left_gdf[['lat_rad','lng_rad']])
    right_radians = np.array(right[['lat_rad','lng_rad']])

    # Find the nearest points
    # -----------------------
    # closest ==> index in right_gdf that corresponds to the closest point
    # dist ==> distance between the nearest neighbors (in meters)

    closest, dist = get_nearest(src_points=left_radians, candidates=right_radians)

    # Return points from right GeoDataFrame that are closest to points in left GeoDataFrame
    closest_points = right.loc[closest]

    # Ensure that the index corresponds the one in left_gdf
    closest_points = closest_points.reset_index(drop=True)

    # Add distance if requested
    if return_dist:
        # Convert to meters from radians
        earth_radius = 6371.0088  # kilometers
        closest_points['distance'] = dist * earth_radius

    return closest_points