import argparse
from logparser import LogParser
from validatefilepath import InputFileValidator


parser = argparse.ArgumentParser(description="Simple LogParser which checks for string in specified file")
parser.add_argument("file_to_parse")
parser.add_argument("string_to_be_found")
args = parser.parse_args()
file_to_parse = args.file_to_parse
string_to_be_found = args.string_to_be_found
Validator = InputFileValidator(file_to_parse)

if Validator.validate():
    result = ""
    for file in Validator.get_files_list():
        added = LogParser.parse_log(file, string_to_be_found)
        #if added:
            #result += "Plik {}:\n".format(file)
            #result += "\n".join(added) + "\n\n"
   # if len(result) > 0:
       # print(result)
       # logs = open("logged_text.log", "w")
       # logs.write(result)
       # logs.close()
else:
    raise FileNotFoundError("Nie znaleziono pliku {}".format(file_to_parse))
