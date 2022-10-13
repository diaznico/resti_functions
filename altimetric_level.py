
import geopandas as gpd
import pandas as pd

def explotar(df):
    """ Transforma elementos de una lista en una fila
    
        devuelve Listas ampliadas a filas de las columnas del 
        subconjunto; index se duplicará para estas filas.
        
            Parameters
            ----------
            df : .dxf
        
            Returns
            -------
            df : .dxf
                devuelve el mismo dxf de entrada, modificado. """

    
    #explode() transforma cada elemento de una lista en una fila replicando
    #los valores del indice.
    df = df.explode()
    
    #reset_index restablece el indice del dataFrame y usa el predeterminado
    #en su lugar DataFrame tiene un MultiIndex, este método puede eliminar
    #uno o más niveles.
    #level = Solo elimine los niveles dados del índice. Elimina todos los 
    #niveles de forma predeterminada.
    
    #drop = No intente insertar un índice en las columnas del marco de datos. 
    #Esto restablece el índice al índice entero predeterminado.
    df = df.reset_index(level=None, drop=True)
    
    return df


def generar_cota_altimetrica(df, layers_a_formatear):
    """ Genera cota altimetrica
        
        genera una cota altimetrica que calcula la distancia vertical 
        que hay desde un punto del terreno, se toma como referencia 
        la altura sobre el nivel del mar.

            Parameters
            ----------
            df : .dxf
            layers_a_formatear : .dxf
                
            Returns
            -------
            layers_a_formatear : .dxf """
    
    
    #accede a un grupo de filas y columnas y cambia nombre.
    df = df.loc[(df['Layer'] == "A_COTA_ALTIMETRICA")]
    #funcion explotar(df)
    df = explotar(df)
    
    #el metodo apply() aplica una funcion a lo largo de uno delos ejes 
    #del DataFrame. 
    #axis = 0 (indice) axis=1 (columnas)
    df['X'] = df.apply(lambda y: y['geometry'].x, axis=1)     
    df['Y'] = df.apply(lambda x: x['geometry'].y, axis=1)
    df['Z'] = df.apply(lambda x: x['geometry'].z, axis=1)   

    df = df[['geometry','X','Y','Z']]
    
    #redondea decimales
    df = df.round(3)
    
    #se escribe un archivo de forma ESRI, pero se puede escribir en 
    #cualquier fuente de datos OGR compatible con fiona
    # output_gpkg == directorio del output.
    df.to_file(output_gpkg, layer='A_COTA_ALTIMETRICA', driver="GPKG")
    
    #borra "A_COTA_ALTIMETRICA
    layers_a_formatear.remove("A_COTA_ALTIMETRICA")
    return layers_a_formatear    

