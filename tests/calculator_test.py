"""Testing the Calculator"""

from calculator.main import Calculator


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    # Act by calling the method to be tested
    result = Calculator.add_number(5.0, 7)
    # Assert that the results are correct
    assert result == 12.0


def test_calculator_subtract():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    # Act by calling the method to be tested
    result = Calculator.subtract_number(5.0, 7)
    # Assert that the results are correct
    assert result == -2.0


def test_calculator_multiply():
    """Testing the multiply function of the calculator"""
    # Arrange by instantiating the calc class
    # Act by calling the method to be tested
    result = Calculator.multiply_number(5.0, 7)
    # Assert that the results are correct
    assert result == 35.0
