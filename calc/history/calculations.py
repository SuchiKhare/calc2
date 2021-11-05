"""Calculation history Class"""


class Calculations:
    """calculations for history - clear, count, first calculation,
    last calculation, get calculations, add calculations """

    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """count history items"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """get last calculation from the history"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """get first calculation from the history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
