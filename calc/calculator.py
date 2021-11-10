"""Main Calculator"""
from calc.history.calculations import Calculations


# This class just call the methods to calculate
class Calculator:
    """calculator class"""

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """adds elements in tuple"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def get_last_calculation_object():
        """get the first result value """
        return Calculations.get_last_calculation_object()
