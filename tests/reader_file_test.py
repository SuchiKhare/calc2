"""Test csv file reading"""
from calc.file_utils.reader_file import CSVFileReader


def test_read_csv_file():
    """Test if file after reading is empty or not"""
    file_name = "addition.csv"
    df_test_csv_data = CSVFileReader(file_name).read_csv_file()
    assert df_test_csv_data is not None
