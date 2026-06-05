import pandas as pd

from app.pipeline.transform import contact_data_frames

df_1 = pd.DataFrame({'coluna_1': [1, 2], 'coluna_2': [3, 4]})
df_2 = pd.DataFrame({'coluna_1': [5, 6], 'coluna_2': [7, 8]})


def testar_a_concatenacao_da_lista_de_dataframes():
    """use o arrange act e assert para testar a função contact_data_frames"""

    # arrange
    lista_de_dataframes = [df_1, df_2]
    lista_de_frames = pd.concat(lista_de_dataframes, ignore_index=True)

    # act
    df_concatenado = contact_data_frames(lista_de_dataframes)

    # assert
    assert df_concatenado.shape == (4, 2)
    assert lista_de_frames.equals(df_concatenado)
