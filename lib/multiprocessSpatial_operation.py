
import geopandas


def mpSpatialJoin(gdfLeft, gdfRigth):
    gdf_LeftJoin = geopandas.sjoin(gdfLeft,
        gdfRigth,
        how="left"
    )
    gdf_LeftJoin.drop("index_right", axis=1, inplace=True)

    return gdf_LeftJoin



