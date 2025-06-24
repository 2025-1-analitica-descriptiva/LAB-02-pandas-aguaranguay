"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
from pathlib import Path


def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
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
    
    return tbl0.groupby('c1')['c2'].sum()
