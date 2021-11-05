"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication


def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    # Arrange
    my_numbers = (1.0, 2.0)
    multiplication = Multiplication(my_numbers)
    # Act
    # Assert
    assert multiplication.get_result() == 2.0
