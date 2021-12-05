"""Test process file data and add data of file"""
from calc.file_utils.reader_file import CSVFileReader
from calc.file_utils.process_file import ProcessData


def test_process_add_file_data():
    """Test file data addition"""
    lst_tuples = [(1, 2), (2, 3)]
    my_dictionary = ProcessData.process_add_file_data(lst_tuples)
    assert isinstance(my_dictionary, dict)


def test_preprocess_file_data():
    """Test convert to list of tuples"""
    file_name = "addition.csv"
    df_test_csv_data = CSVFileReader(file_name).read_csv_file()
    assert df_test_csv_data is not None


def test_process_subtract_file_data():
    """Test file data addition"""
    lst_tuples = [(1, 2), (2, 3)]
    my_dictionary = ProcessData.process_subtract_file_data(lst_tuples)
    assert isinstance(my_dictionary, dict)


def test_process_multiply_file_data():
    """Test file data addition"""
    lst_tuples = [(1, 2), (2, 3)]
    my_dictionary = ProcessData.process_multiply_file_data(lst_tuples)
    assert isinstance(my_dictionary, dict)


def test_process_divide_file_data():
    """Test file data addition"""
    lst_tuples = [(1, 2), (2, 3)]
    my_dictionary = ProcessData.process_division_file_data(lst_tuples)
    assert isinstance(my_dictionary, dict)
