import geopandas as gpd
import pandas as pd
from shapely.geometry import shape, LineString, Polygon

def lineas_a_poligonos(df):
    """ Convert a string of lines to polygons

    Args:
        df (dxf): Lines

    Returns:
        dxf: lines converted to polygons """

    for index, row in df.iterrows():
        linea = shape(row['geometry'])
        coordenadas = []
        
        if isinstance(linea, LineString):
            for index, point in enumerate(linea.coords):
                if index == 0:
                    primer_punto = point
                coordenadas.append(point)
            coordenadas.append(primer_punto)

            if len(coordenadas) >= 3:
                poligono = Polygon(coordenadas)
                pol = gpd.GeoSeries(poligono)
                
    return pol

