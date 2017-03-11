from os.path import isfile


class LogParser:
    @staticmethod
    def parse_log(input_file, string_to_be_found):
        if isfile(input_file):
            with open(input_file) as file:
                lines = []
                for line in file:
                    line = line.strip()
                    lines.append(line)
                matching_lines = [x for x in lines if string_to_be_found in x]
                return matching_lines
        else:
            raise FileNotFoundError("Brak pliku")

