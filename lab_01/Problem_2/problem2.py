import argparse
from validatefilepath import InputFileValidator
from wordcounter import WordCounter

parser = argparse.ArgumentParser(description="Argumenty wejsciowe")
parser.add_argument("file_to_parse", help="File where you'll be counting words")
args = parser.parse_args()
file_to_parse = args.file_to_parse
Validator = InputFileValidator(file_to_parse)

if Validator.validate():
    for file in Validator.get_files_list():
        WordCounter.Count(file_to_parse)