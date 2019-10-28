# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:34:02 2019

@author: Aspen HYSYS
"""

import PySimpleGUI as sg
import numpy as np
import pandas as pd
import os
from functools import reduce

######################################################## FUNCIONES REQUERIDAS


########## ABRIR ARCHIVO

def abrir_df(archivo, formato = 'csv'):
    
    '''Abre un archivo de csv o excel indistintamente de si el separador es ; o ,'''
    
    if formato == 'csv': 
        
        df = pd.read_csv(archivo, nrows = 1)
    
        if len(df.columns) == 1: 
            
            df = pd.read_csv(archivo, sep = ";", dtype = str)
            
        else: 
            
            df = pd.read_csv(archivo, dtype = str)
            
    else: 
        
        df = pd.read_excel(archivo, nrows = 1)
    
        if len(df.columns) == 1: 
            
            df = pd.read_excel(archivo, sep = ";", dtype = str)
            
        else: 
            
            df = pd.read_excel(archivo, dtype = str)
        
        
    return df

########## GUARDAR ARCHIVO
    
def guardar_archivo(df, nombre, formato = 'excel', ruta = os.getcwd() ): 
    
    if formato == 'csv': 
        
        df.to_csv(f'{ruta}\\{nombre}.csv', index = True, header = True)
        
    else:
        
        df.to_excel(f'{ruta}\\{nombre}.xlsx', index = True, header = True)
        
    status = f'archivo {nombre} guardado en {ruta}'
    
    return status

########## COLUMNAS REPETIDAS

def eliminar_col_dup(df): 
    
    y_col = [x for x in df.columns if x.endswith("_x")]
    
    x_col = [x for x in df.columns if x.endswith("_y")]
    
    col_new = [x.split("_")[0] for x in x_col]

    x_col.sort(), y_col.sort(), col_new.sort()

    for column in range(len(col_new)):

        df[col_new[column]] = np.where(df[x_col[column]].isnull(), df[y_col[column]], df[x_col[column]]) 

    # ELIMINAR x_col  e y_col  -------------------------------------------------

    df.drop(x_col, axis=1, inplace=True)
    df.drop(y_col, axis=1, inplace=True)   

    # ELIMINAR DUPLICADOS  -------------------------------------------------


    df = df.loc[~df.index.duplicated(keep = "first")] 
    
    return df

########## UNIR ARCHIVOS

def unir_archivos(archivos, formato = 'csv'): 
    
    df_list = []
    
    for archivo in archivos:
        
        print(archivo)
    
        df = abrir_df(archivo, formato)
        
        df['Estampa de tiempo'] = pd.to_datetime(df['Estampa de tiempo'])
        
        df.set_index('Estampa de tiempo', inplace = True)
        
        df_list.append(df)
        
        print(len(df_list))
        
    df = reduce(lambda x,y: eliminar_col_dup(pd.merge(x,y, on = 'Estampa de tiempo', how = 'outer')), df_list)
       
    return df
    

files = sg.PopupGetFile('Seleccione los archivos', multiple_files = True)

files = files.split(";")

print('good1')

df = unir_archivos(files, 'csv')
print('good2')
#status = guardar_archivo(df, 'PRUEBA NENE')

print('good3')

#sg.Popup(status)


