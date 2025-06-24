"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    path0 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl0.tsv"
    path1 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl1.tsv"
    path2 = r"C:\Users\Alejo\Documents\GitHub\LAB-02-pandas-aguaranguay\files\input\tbl2.tsv"

    tbl0 = pd.read_csv(path0, sep='\t')
    tbl1 = pd.read_csv(path1, sep='\t')
    tbl2 = pd.read_csv(path2, sep='\t')
    
    merged = tbl0.merge(tbl2, on='c0')
    return merged.groupby('c1')['c5b'].sum()
