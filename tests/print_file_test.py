"""Test Print contents to a file"""
from calc.file_utils.print_file import PrintContent


def test_print_content():
    """Test forms the list of all contents"""
    lst_contents = []
    content1 = "2021-12-03 19:01:45.202205    Addition    1 1     2.0"
    content2 = "2021-12-03 19:01:45.202205    Addition    999 100     1099.0"
    lst_contents.append(content1)
    lst_contents.append(content2)
    is_written = PrintContent(lst_contents).print_content("log.txt")
    assert is_written is True
