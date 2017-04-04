from os.path import isfile
import re


class LogParser:
    @staticmethod
    def parse_log(input_file, string_to_be_found):
        if isfile(input_file):
            data = []
            with open(input_file) as file:
                lines = []
                for line in file:
                    line = line.strip()
                    lines.append(line)
                matching_lines = [x for x in lines if string_to_be_found in x and "****" not in x]
                for i in range(0, len(matching_lines)):
                    matching_lines[i] = re.sub(" +", " ", matching_lines[i])
                    matching_lines[i] = re.sub(" %", "", matching_lines[i])
                    matching_lines[i] = re.sub("^.+INFO ([^ ]+) ?.+purity: (.*), hitEff: (.*)", r"\1 \2 \3", matching_lines[i])
                if "PrChecker.Downs... INFO" in matching_lines:
                    matching_lines.remove("PrChecker.Downs... INFO")
                for line in matching_lines:
                    data.append(line.split(" "))
                return data
        else:
            raise FileNotFoundError("Brak pliku")
