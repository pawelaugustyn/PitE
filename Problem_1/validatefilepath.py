from os import listdir
from os.path import isdir
from os.path import isfile
from os.path import join


class InputFileValidator:
    def __init__(self, file_path):
        self._files = []
        self._file_path = file_path

    def get_files_list(self):
        return self._files

    def validate(self):
        if isdir(self._file_path):
            self._files = [self._file_path
                           + "/"
                           + single_file for single_file in listdir(self._file_path)
                           if isfile(join(self._file_path, single_file))]
            if len(self._files):
                return True
            else:
                return False
        elif isfile(self._file_path):
            self._files.append(self._file_path)
            return True
        else:
            return False
