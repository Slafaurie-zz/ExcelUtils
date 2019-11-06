# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:32:21 2019

@author: Aspen HYSYS
"""

import numpy as np

def eliminar_duplicadas(df): 
    
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
