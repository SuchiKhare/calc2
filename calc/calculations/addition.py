"""Class for Addition Operation"""
from calc.calculations.operation import Operation


class Addition(Operation):
    """subclass Addition extending base Operation"""

    def get_output(self):
        """Adds the elements in tuple"""
        sum_of_elements = 0.0
        for value in self.values:
            sum_of_elements = sum_of_elements + value
        return sum_of_elements
