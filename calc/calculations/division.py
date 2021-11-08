"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        result = 1.0
        try:
            for value in self.values:
                result = result / value
            my_formatter = "{0:.2f}"
            result = my_formatter.format(result)
        except ZeroDivisionError as my_err:
            raise ZeroDivisionError from my_err
        return result
