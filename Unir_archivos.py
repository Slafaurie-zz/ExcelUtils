
'''Realiza un inner join de una serie de archivos.''''

import pandas as pd
from functools import reduce 

def unir_archivos(archivos, columna): 
        
    df_list = [pd.read_csv(archivo) for archivo in archivos]
        
    df = reduce(lambda x,y: pd.merge(x,y, on = columna ), df_list)
    
    return df
