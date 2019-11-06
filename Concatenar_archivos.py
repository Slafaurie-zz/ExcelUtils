
####################################################### Importar librerias

import PySimpleGUI as sg
import pandas as pd
import os
import itertools

  

####################################################### GUI
  
layout = [[sg.Text('Seleccionar', size = (12,1)), sg.Input(justification = 'left'), sg.FilesBrowse('Buscar')], 
           [sg.Text('Guardar como', size = (12,1)), sg.Input(justification = 'left')],
           [sg.Text('Carpeta', size = (12,1)), sg.Input(justification = 'left'), sg.FolderBrowse('Buscar')],
           [sg.CloseButton(button_text = 'Aceptar'), sg.CloseButton('Salir')]]


event, values = sg.Window('Excel Merger', layout).Read()

####################################################### Abrir archivos

def abrir_df(archivo):
    
    formato = archivo.split(".")[-1]
    
    
    if formato == 'xlsx':
        
        df = pd.read_excel(archivo, dtype = str)
        
    elif formato == 'csv': 
        
        df = pd.read_csv(archivo, nrows = 0)
    
        if len(df.columns) > 1: 
            
            df = pd.read_csv(archivo, dtype = str)
            
        else: 
            
            df = pd.read_csv(archivo, sep = ";", dtype = str)
            
    else: 
        
        df = pd.read_csv(archivo, nrows = 1, sep = " ")
        
        if len(df.columns) > 1: 
            
            df = pd.read_csv(archivo, sep = " ", dtype = str)
        
        else: 
            
            df = pd.read_csv(archivo, sep = ";")
        
    return df

####################################################### columnas unicas
    
def col_unicas(archivos_carpeta): 
    
    
    columnas = ([abrir_df(archivo).columns.values.tolist() for archivo in archivos_carpeta])
    
    columnas_flat = list(itertools.chain.from_iterable(columnas))

    unicos = list(set(columnas_flat))
    
    return unicos

####################################################### concatenar archivos

def concatenar_archivos(archivos_carpeta, unicos = None, nombre = None, ruta = os.getcwd()):

    for idx, archivo in enumerate(archivos_carpeta): 
    
        df = abrir_df(archivo)
        
        df = pd.concat([df,pd.DataFrame(columns = [x for x in unicos if x not in df.columns])], sort = True)
        
        if idx == 0: 
            
            df.to_csv(f'{ruta}\\{nombre}.csv', header = True, index = False)
            
        else: 
            
            df.to_csv(f'{ruta}\\{nombre}.csv', header = False, index = False, mode = "a")

    status = f'archivo {nombre} guardado en {ruta}'
    
    return status


####################################################### Codigo 


archivos = values['Buscar'].split(";")

nombre_archivo = values[1]

ruta_guardar = values['Buscar0']

unicos = col_unicas(archivos)

status = concatenar_archivos(archivos, unicos, nombre_archivo, ruta_guardar)

sg.Popup(status)

