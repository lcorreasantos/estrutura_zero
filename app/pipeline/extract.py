"""Módulo de extração de dados."""

import glob  # lib para listar arquivos
import os  # lib para manipular arquivos e pastas
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Read Excel files from a folder and return a list of dataframes.

    Args:
        path: Folder path with the Excel files.

    Returns:
        List of dataframes read from the Excel files.
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


"""
O código abaixo é utilizado para testar a função extract_from_excel 
executando diretamente este arquivo, sem precisar chamar/importar a 
função em outro arquivo.
"""

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(data_frame_list)
