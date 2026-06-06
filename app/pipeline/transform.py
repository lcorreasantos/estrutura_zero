"""Módulo de transformação de dados."""

from typing import List

import pandas as pd


def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Return a single dataframe from a list of dataframes."""
    return pd.concat(data_frame_list, ignore_index=True)
