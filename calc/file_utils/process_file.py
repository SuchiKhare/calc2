"""Process file data and add data of file"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations


class ProcessData:
    """Reader Class"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def preprocess_file_data(file_df):
        """"convert to list of tuples"""
        records = file_df.to_records(index=False)
        print("type of records is ", type(records))
        lst_tuples = list(records)
        return lst_tuples

    @staticmethod
    def process_add_file_data(lst_tuples):
        """file data addition"""
        my_dictionary = {}
        for my_tuple in lst_tuples:
            print(my_tuple)
            is_added = Calculator.add_numbers(my_tuple)
            print("result_tuple, is_added", Calculations.get_last_calculation_result_value())
            my_dictionary[str(my_tuple)] = Calculations.get_last_calculation_result_value()
        return my_dictionary, is_added

