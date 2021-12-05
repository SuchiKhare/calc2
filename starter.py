"""Defining main function"""
from calc.file_utils.archive_file import ArchiveFile
from calc.file_utils.content_file import FormContent
from calc.file_utils.reader_file import CSVFileReader

from calc.file_utils.print_file import PrintContent
from calc.file_utils.process_file import ProcessData


def main():
    file_name = "division.csv"
    file_df = CSVFileReader(file_name).read_csv_file()
    print(file_df)
    lst_tuples = ProcessData.preprocess_file_data(file_df)
    print("list of tuples to process ", lst_tuples)
    operation_name = "Division"
    my_dictionary = ProcessData.process_division_file_data(lst_tuples)
    print("my_dictionary = ", my_dictionary)

    # unix time stamp, filename of the input file, record number, operation, and result of the calculation
    lst_contents = FormContent(file_name, operation_name, my_dictionary).get_all_content()
    is_written = PrintContent(lst_contents).print_content("log.txt")
    if is_written:
        is_archived = ArchiveFile.archive_file(file_name)
        print("Archived = ", is_archived)


if __name__ == "__main__":
    main()
