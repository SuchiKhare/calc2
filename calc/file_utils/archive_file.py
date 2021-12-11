"""Archive the file"""
# import shutil


class ArchiveFile:
    """Archive the file"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def archive_file(file_name):
        """archive the file"""
        # files = [file_name]
        # source = 'C:/Users/SuchiK/PycharmProjects/calc2_csv/tests/test_data/'
        # destination = 'C:/Users/SuchiK/PycharmProjects/calc2_csv/archived/'
        # shutil.move(source + file_name, destination + file_name)
        source = '../../tests/test_data/'
        destination = 'archived/'
        shutil.move(source + file_name, destination + file_name)
        print("file_name ", file_name)
        return True
