"""Test Archive the file"""
from calc.file_utils.archive_file import ArchiveFile


# pylint: disable=too-few-public-methods
def test_archive_file():
    """Test archive the file"""
    is_archived = ArchiveFile.archive_file("addition.csv")
    assert is_archived is True
