"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
from pathlib import Path


def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """


    # Carpeta input relativa a la raíz del repo
    INPUT_DIR = Path("files/input")

    # Archivos
    path0 = INPUT_DIR / "tbl0.tsv"
    path1 = INPUT_DIR / "tbl1.tsv"
    path2 = INPUT_DIR / "tbl2.tsv"

    tbl0 = pd.read_csv(path0, sep='\t')
    tbl1 = pd.read_csv(path1, sep='\t')
    tbl2 = pd.read_csv(path2, sep='\t')
    
    return tbl0.groupby('c1')['c2'].max()
