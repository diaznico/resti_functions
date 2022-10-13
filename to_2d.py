
import geopandas as gpd
import pandas as pd
from shapely.ops import transform, linemerge #, polygonize


def to_2D(df):
    """ Transform to 2D
    function transforms to 2D modeling, does not use the
    Z axis depth, width and length only (x,y)

    Args:
        df (dxf): _description_
    """

    geometria_2d = []
    for index, row in df.iterrows():

        #Utiliza la clase transform() de shapely para expresar que no hay geometria de tipo Z 
        geometria_2d.append(transform(lambda x, y, z=None: (x, y), 
                                      row['geometry']))
        
    df.geometry = geometria_2d
    return df


