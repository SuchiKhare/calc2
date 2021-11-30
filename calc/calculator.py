"""Main Calculator"""
from calc.history.calculations import Calculations


# This class just call the methods to calculate
class Calculator:
    """calculator class"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def add_numbers(tuple_elements: tuple):
        """adds elements in tuple"""
        Calculations.add_addition_calculation(tuple_elements)
        return True

    @staticmethod
    def subtract_numbers(tuple_elements: tuple):
        """subtract elements in tuple"""
        Calculations.add_subtraction_calculation(tuple_elements)
        return True

    @staticmethod
    def multiply_numbers(tuple_elements: tuple):
        """multiply elements in tuple"""
        Calculations.add_multiplication_calculation(tuple_elements)
        return True

    @staticmethod
    def divide_numbers(tuple_elements: tuple):
        """divide elements in tuple"""
        Calculations.add_division_calculation(tuple_elements)
        return True
