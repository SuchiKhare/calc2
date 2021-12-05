"""Print contents to a file"""
from pathlib import Path


class PrintContent:
    """Reader Class"""

    # unix time stamp, filename of the input file, record number
    # operation, and result of the calculation

    # pylint: disable=too-few-public-methods
    def __init__(self, lst_contents):
        """PrintContent parametrized constructor"""
        self.lst_contents = lst_contents

    # pylint: disable=too-few-public-methods
    def print_content(self, log_file_name):
        """print or write the contents to file"""
        for contents in self.lst_contents:
            file_n = "logging/" + log_file_name
            with open(file_n, 'a', encoding="utf-8") as file_to_open:
                my_file = Path(file_n)
                print("Path of file to open ", my_file)
                print("is that a file ", contents)
                file_to_open.writelines(contents + "\n")
                print("written")
        return True
