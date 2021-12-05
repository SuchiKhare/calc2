"""Read external file"""
import os
from pathlib import Path

import pandas as pd


class CSVFileReader:
    # pylint: disable=too-few-public-methods

    """Reader Class"""

    def __init__(self, file_name):
        """"""
        self._file_name = file_name

    # pylint: disable=too-few-public-methods
    def read_csv_file(self):
        """Read CSV into pandas dataframe"""
        my_directory = os.path.dirname(os.path.realpath(__file__))
        print("my_directory", my_directory)
        levels_up = 2
        print(Path(my_directory).parents[levels_up - 1])
        file_path = os.path.join(Path(my_directory).parents[levels_up - 1], "tests/test_data",
                                 self._file_name)
        print("file_path", file_path)
        file_df = pd.read_csv(file_path, header=None, error_bad_lines=False)
        return file_df.iloc[1:, 1:]  # to drop result and header
