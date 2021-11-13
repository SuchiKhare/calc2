"""Class for Subtraction Operation"""
from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Subtraction(Operation, Result):
    """subclass Subtraction extending base Operation"""

    # This is the instance method
    def get_output(self):
        """Subtract the elements in tuple and return"""
        diff_of_elements = 0.0
        for value in self._values:
            diff_of_elements = diff_of_elements + value
        return diff_of_elements
