"""Testing Addition"""
import pytest

from calc.calculations.division import Division


def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    # Arrange
    my_numbers = (3.0, 1.0, 1.5)
    division = Division(my_numbers)
    # Act
    # Assert
    assert division.get_result() == "0.22"
    with pytest.raises(ZeroDivisionError):
        value = Division((1.0, 0.0, 1.0))
        assert value.get_result() == 1.0
