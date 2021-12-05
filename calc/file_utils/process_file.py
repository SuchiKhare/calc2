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
        my_dictionary = {}
        for my_tuple in lst_tuples:
            build_dict_key = ""
            print(my_tuple)
            for item in my_tuple:
                build_dict_key = build_dict_key + str(item) + " "
            print("build_dict_key = ", build_dict_key)
            Calculator.add_numbers(my_tuple)
            result_tuple = Calculations.get_last_calculation_result_value()
            print("result_tuple", result_tuple)
            my_dictionary[build_dict_key] = Calculations.get_last_calculation_result_value()
        return my_dictionary

    @staticmethod
    def process_subtract_file_data(lst_tuples):
        my_dictionary = {}
        for my_tuple in lst_tuples:
            build_dict_key = ""
            print(my_tuple)
            for item in my_tuple:
                build_dict_key = build_dict_key + str(item) + " "
            print("build_dict_key = ", build_dict_key)
            Calculator.subtract_numbers(my_tuple)
            result_tuple = Calculations.get_last_calculation_result_value()
            print("result_tuple", result_tuple)
            my_dictionary[build_dict_key] = Calculations.get_last_calculation_result_value()
        return my_dictionary

    @staticmethod
    def process_multiply_file_data(lst_tuples):
        my_dictionary = {}
        for my_tuple in lst_tuples:
            build_dict_key = ""
            print(my_tuple)
            for item in my_tuple:
                build_dict_key = build_dict_key + str(item) + " "
            print("build_dict_key = ", build_dict_key)
            Calculator.multiply_numbers(my_tuple)
            result_tuple = Calculations.get_last_calculation_result_value()
            print("result_tuple", result_tuple)
            my_dictionary[build_dict_key] = Calculations.get_last_calculation_result_value()
        return my_dictionary

    @staticmethod
    def process_division_file_data(lst_tuples):
        my_dictionary = {}
        for my_tuple in lst_tuples:
            build_dict_key = ""
            print(my_tuple)
            for item in my_tuple:
                build_dict_key = build_dict_key + str(item) + " "
            print("build_dict_key = ", build_dict_key)
            Calculator.divide_numbers(my_tuple)
            result_tuple = Calculations.get_last_calculation_result_value()
            print("result_tuple", result_tuple)
            my_dictionary[build_dict_key] = Calculations.get_last_calculation_result_value()
        return my_dictionary

