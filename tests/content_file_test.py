"""Test Get all contents for print"""
from datetime import datetime

from calc.file_utils.content_file import FormContent


def test_get_all_content():
    """Test forms the list of all contents"""
    lst_contents = []
    file_name = "addition.csv"
    operation_name = "Addition"
    # my_dictionary = {"1 1": 2.0}
    my_dictionary = {'1 1 ': 2.0, '2 3 ': 5.0, '999 100 ': 1099.0
        , '1.5 1.5 ': 3.0, '1.5 2.5 ': 4.0, '3.0 3 ': 6.0}
    lst_contents = FormContent(file_name, operation_name, my_dictionary).get_all_content()
    assert len(lst_contents) == 6
    # 2021-12-03 19:01:45.202205    Addition    1 1     2.0


def test_get_time():
    """Test time time returns the unix timestamp"""
    my_date_object = FormContent.get_time()
    assert isinstance(my_date_object, datetime)
