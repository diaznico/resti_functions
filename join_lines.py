
import geopandas as gpd
import pandas as pd
from shapely.ops import transform, linemerge #, polygonize


def unirLineas(df):
    """ Unify lines
    
       Function unifies the lines that are individual before doing
        a conversion to polygons or just to unify them.
    
            Parameters
            ----------
            df : .dxf
                
            Returns
            -------
            df : .dxf
                
        note: works if lines are contiguous 'points match
        queues' but if they are not contiguous (there is a space between them)
        returns another multiLineString."""

    geometrias = list(df.geometry)
    unir_lineas = linemerge(geometrias)
        
    try:
        geometria_lista = [i for i in unir_lineas]
    except TypeError:
        geometria_lista = [unir_lineas]
        
    df = gpd.GeoDataFrame(geometry = geometria_lista)
    #reference system.
    df.crs = "EPSG:5348"
    return df

