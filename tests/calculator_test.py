"""Testing the Calculator"""

import pytest

from calculator.main import Calculator


def test_calculator_add():
    """ Testing the Add function of the calculator """
    assert Calculator.add_number(15, 3) == 18


def test_calculator_subtract():
    """ Testing the subtract function of the calculator """
    assert Calculator.subtract_number(15, 3) == 12


def test_calculator_multiply():
    """ Testing the multiply function of the calculator """
    assert Calculator.multiply_numbers(15, 3) == 45


def test_calculator_divide():
    """ Testing the divide function of the calculator """
    assert Calculator.divide_numbers(15, 3) == 5
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(15, 0)
