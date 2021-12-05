"""Get all contents for print"""
# unix time stamp, filename of the input file,
# record number, operation, and result of the calculation

import time
from datetime import datetime


class FormContent:
    """Reader Class"""

    def __init__(self, file_name, operation_name, _my_dictionary):
        """parameterized constructor """
        self._file_name = file_name
        self._operation_name = operation_name
        self._my_dictionary = _my_dictionary

    @staticmethod
    def get_time():
        """time time returns the unix timestamp"""
        my_date_object = datetime.fromtimestamp(time.time())
        print("Check Times ", my_date_object, type(my_date_object))
        return my_date_object
        # 2021-12-03 19:01:45.202205 <class 'datetime.datetime'>

    def get_all_content(self):
        """forms the list of all contents"""
        my_date_object = FormContent.get_time()
        lst_contents = []
        for x_keys, y_values in self._my_dictionary.items():
            contents = str(my_date_object) + "    " + self._operation_name +\
                       "    " + str(x_keys) + "    " + str(
                y_values)
            print("contents are ", contents)
            lst_contents.append(contents)
        return lst_contents
