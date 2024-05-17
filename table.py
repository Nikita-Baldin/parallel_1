import json
import os
import logging
import pandas as pd
import dataframe_image as dfi

logger = logging.getLogger()
logger.setLevel("INFO")


def create_and_save_table(json_file, path_to_folder):
    """
    Функция создает таблицу
    :data_file: данные для создания
    :return: None
    """
    with open(json_file, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.columns.name = 'Time / Size'
    df.loc['mean'] = df.mean()
    first_row = df.iloc[0]
    sorted_df = df[first_row.sort_values().index]
    dfi.export(sorted_df, os.path.join(path_to_folder, "table.png"))
    logging.info("Table saved")