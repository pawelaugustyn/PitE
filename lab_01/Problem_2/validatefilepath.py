from os.path import isfile


class InputFileValidator:
    @staticmethod
    def validate(file_path):
        if isfile(file_path):
            return True
        else:
            return False
