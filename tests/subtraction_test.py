"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction
from tests.panda_extract_data import PandaExtractData

def test_static_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    filename = "subtraction_1000values.xlsx"
    df_values = PandaExtractData.read_file(filename)
    for index, row in df_values.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        subtraction = Subtraction.create(tuple_values)
    #Assert
        assert subtraction.get_result() == df_values['result'][index]
