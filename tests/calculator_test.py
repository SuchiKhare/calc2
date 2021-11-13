"""Testing the Calculator"""
import pytest

from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """fixture method and will run each time we pass it to a test"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


def test_add_numbers(clear_history_fixture):
    """test addition of numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (10.0, 20.0, 30.0)
    Calculator.add_numbers(numbers)
    assert Calculations.get_first_calculation().get_output() == 60.0
    assert isinstance(Calculations.get_last_calculation_object(), Addition)


def test_subtract_numbers(clear_history_fixture):
    """test subtraction of numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (10.0, 20.0, 30.0, 10.0)
    Calculator.subtract_numbers(numbers)
    assert Calculations.get_first_calculation().get_output() == 70.0
    assert isinstance(Calculations.get_last_calculation_object(), Subtraction)


def test_multiply_numbers(clear_history_fixture):
    """test multiplication of numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (1.0, 2.0, 3.0, 4.0)
    Calculator.multiply_numbers(numbers)
    assert Calculations.get_first_calculation().get_output() == 24.0
    assert isinstance(Calculations.get_last_calculation_object(), Multiplication)


def test_divide_numbers(clear_history_fixture):
    """test division of numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Arrange
    my_numbers = (3.0, 1.0, 1.0)
    # division = Division(my_numbers)
    # assert division.get_output() == "0.33"
    Calculator.divide_numbers(my_numbers)
    assert Calculations.get_first_calculation().get_output() == "0.33"
    with pytest.raises(ZeroDivisionError):
        another_no = (1.0, 0.0)
        Calculator.divide_numbers(another_no)
        assert Calculations.get_last_calculation_result_value() == 1.0
    assert isinstance(Calculations.get_last_calculation_object(), Division)
