from os.path import isfile
import re

class LogParser:
    @staticmethod
    def parse_log(input_file, string_to_be_found):
        if isfile(input_file):
            with open(input_file) as file:
                finalarray = []
                lines = []
                for line in file:
                    line = line.strip()
                    lines.append(line)
                matching_lines = [x for x in lines if string_to_be_found in x]
                matching_lines = "\n".join(matching_lines)
                matching_lines = re.sub(' +', ' ', matching_lines)
                matching_lines = re.sub(' clones', ' ', matching_lines)
                matching_lines = re.sub('PrChecker.Downs... INFO ?\n', '', matching_lines)
                matching_lines = re.sub('PrChecker.Downs... INFO ?', ' ', matching_lines)
                matching_lines = re.sub(' +', ' ', matching_lines)
                matching_lines = re.sub('\n+', '\n', matching_lines)
                matching_lines = re.sub('\*+.+\*+', '', matching_lines)
                matching_lines = re.sub(': ', '', matching_lines)
                matching_lines = re.sub('purity', '', matching_lines)
                matching_lines = re.sub('from ', '', matching_lines)
                matching_lines = re.sub('hitEff', '', matching_lines)
                matching_lines = re.sub(', ', ' ', matching_lines)
                matching_lines = re.sub(' %', '%', matching_lines)
                matching_lines = re.sub(' \[', '', matching_lines)
                matching_lines = re.sub('\]', '', matching_lines)
                words = matching_lines.split("\n")
                words = [x for x in words if len(x) > 1]
                for word in words:
                    word = word.split(' ')
                    arraytoinsert = [x for x in word if len(x) > 1]
                    if len(arraytoinsert) > 0 and re.match('[A-Za-z]{1}.+', arraytoinsert[0]):
                        finalarray.append(arraytoinsert)
                return finalarray
        else:
            raise FileNotFoundError("Brak pliku")

