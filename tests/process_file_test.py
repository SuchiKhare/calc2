"""Test process file data and add data of file"""
from calc.file_utils.reader_file import CSVFileReader
from calc.file_utils.process_file import ProcessData


def test_process_add_file_data():
    """Test file data addition"""
    lst_tuples = [(1, 2), (2, 3)]
    my_dictionary, is_added = ProcessData.process_add_file_data(lst_tuples)
    assert isinstance(my_dictionary, dict)
    assert is_added is True


def test_preprocess_file_data():
    """Test convert to list of tuples"""
    file_name = "addition.csv"
    df_test_csv_data = CSVFileReader(file_name).read_csv_file()
    assert df_test_csv_data is not None
