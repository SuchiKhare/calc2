"""Testing the Calculator"""
import pytest

from calc.calculations.operation import Operation
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """fixture method that will run each time you pass it to a test"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


def test_add_numbers(clear_history_fixture):
    """test addition of numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (10.0, 20.0, 30.0)
    Calculator.add_numbers(numbers)
    assert Calculations.get_first_calculation().get_output() == 60.0
    assert isinstance(Calculations.get_last_calculation_object(), Operation)
