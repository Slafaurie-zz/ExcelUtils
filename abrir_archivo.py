
import pandas as pd 

''' Descripcion: Abre un DataFrame a partir de un archivo csv o xlsx teniendo en cuenta si el separador es ; o ,'''

def abrir_df(archivo, indice = None):
    
    formato = archivo.split(".")[-1]
    
    
    if formato == 'xlsx':
        
        df = pd.read_excel(archivo, dtype = str)
        
    elif formato == 'csv': 
        
        df = pd.read_csv(archivo, nrows = 1)
    
        if len(df.columns) > 1: 
            
            df = pd.read_csv(archivo, dtype = str)
            
        else: 
            
            df = pd.read_csv(archivo, sep = ";", dtype = str)
            
    else: 
        
        df = pd.read_csv(archivo, nrows = 1, sep = " ")
        
        if len(df.columns) > 1: 
            
            df = pd.read_csv(archivo, sep = " ", dtype = str)
        
        else: 
            
            df = pd.read_csv(archivo, sep = ",")
        
    
    if not indice: 
        
        return df
        
    else: 
        
        df = df.set_index(indice)
        
        return df
