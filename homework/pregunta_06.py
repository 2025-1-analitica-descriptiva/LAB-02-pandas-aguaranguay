"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    path0 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl0.tsv"
    path1 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl1.tsv"
    path2 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl2.tsv"

    tbl0 = pd.read_csv(path0, sep='\t')
    tbl1 = pd.read_csv(path1, sep='\t')
    tbl2 = pd.read_csv(path2, sep='\t')
    
    return sorted(tbl1['c4'].str.upper().unique())
