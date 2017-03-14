import argparse

from lab_01.Problem_1.validatefilepath import InputFileValidator

from lab_01.Problem_1.logparser import LogParser

parser = argparse.ArgumentParser(description="Simple LogParser which checks for string in specified file")
parser.add_argument("file_to_parse", help="Name of file where you will look for a string")
parser.add_argument("string_to_be_found", help="String that you'll be looking for")
args = parser.parse_args()
file_to_parse = args.file_to_parse
string_to_be_found = args.string_to_be_found
Validator = InputFileValidator(file_to_parse)

if Validator.validate():
    result = ""
    finalarray = []
    for file in Validator.get_files_list():
        added = LogParser.parse_log(file, string_to_be_found)
        if added:
            finalarray = finalarray + added

    for i in range(0, len(finalarray)):
        print(finalarray[i])

else:
    raise FileNotFoundError("Nie znaleziono pliku {}".format(file_to_parse))
