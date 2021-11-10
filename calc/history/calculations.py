"""Calculation history Class"""
from calc.calculations.addition import Addition


class Calculations:
    """Manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get total items in history list"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get object of last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get result of last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_output()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a calculation at particular index of history list"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ add calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Add addition object to history"""
        Calculations.add_calculation(Addition.create_operation(values))
        # Get the result of the calculation
        return True
