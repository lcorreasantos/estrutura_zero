"""Módulo de carga de dados."""

import os  # biblioteca para manipular arquivos e pastas

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """Save a dataframe as an Excel file.

    Args:
        data_frame: Dataframe to save as Excel.
        output_path: Path where the file will be saved.
        file_name: Name of the file to save.

    Returns:
        Success message.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
