import itertools
import pandas as pd
from glob import glob

archivos_carpeta = glob('*.csv')

def col_unicas(archivos_carpeta): 
    
    columnas = ([pd.read_csv(archivo).columns.values.tolist() for archivo in archivos_carpeta])
    
    columnas_flat = list(itertools.chain.from_iterable(columnas))

    unicos = list(set(columnas_flat))
    
    return unicos
