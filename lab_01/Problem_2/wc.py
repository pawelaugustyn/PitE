import argparse, sys, os, logging
from validatefilepath import InputFileValidator


class WordCounter:
    def __init__(self, args):
        self._wordsCounter = {}
        self._linesCounter = {}
        self._charsCounter = {}

        log_file_name = "wc.log"
        if os.path.isfile(log_file_name):
            os.remove(log_file_name)
        logging.basicConfig(filename=log_file_name, level=logging.INFO)

        self._args = args
        self._files = []

        for filename in self._args.input_files:
            if InputFileValidator.validate(filename):
                logging.info("File %s exists", filename)
                self._files.append(filename)
            else:
                logging.info("File %s not found", filename)
                sys.exit(0)

    def count_lines_in_all_files(self):
        for file in self._files:
            self._linesCounter[file] = self._count_lines_in_single_file(file)

    def count_words_in_all_files(self):
        for file in self._files:
            self._wordsCounter[file] = self._count_words_in_single_file(file)

    def count_chars_in_all_files(self):
        for file in self._files:
            self._charsCounter[file] = self._count_chars_in_single_file(file)

    @staticmethod
    def _count_lines_in_single_file(file):
        data = open(file, "r").read()
        return len(data.splitlines())

    @staticmethod
    def _count_words_in_single_file(file):
        data = open(file, "r").read()
        return len(data.split())

    @staticmethod
    def _count_chars_in_single_file(file):
        data = open(file, "r").read()
        return len(data)

    def print_logs_to_file(self):
        if not len(self._files):
            return None
        if self._args.lines:
            if self._args.words:
                if self._args.chars:
                    logging.info("Lines\tWords\tChars")
                else:
                    logging.info("Lines\tWords")
            else:
                if self._args.chars:
                    logging.info("Lines\tChars")
                else:
                    logging.info("Lines\t")
        else:
            if self._args.words:
                if self._args.chars:
                    logging.info("Words\tChars")
                else:
                    logging.info("Words")
            else:
                if self._args.chars:
                    logging.info("Chars")
                else:
                    return None

        for file in self._files:
            string = ""
            if self._args.lines:
                if self._args.words:
                    if self._args.chars:
                        string += str(self._linesCounter[file]) + "\t" + str(self._wordsCounter[file]) + "\t" + str(self._charsCounter[file])
                    else:
                        string += str(self._linesCounter[file]) + "\t" + str(self._wordsCounter[file])
                else:
                    if self._args.chars:
                        string += str(self._linesCounter[file]) + "\t" + str(self._charsCounter[file])
                    else:
                        string += str(self._linesCounter[file])
            else:
                if self._args.words:
                    if self._args.chars:
                        string += str(self._wordsCounter[file]) + "\t" + str(self._charsCounter[file])
                    else:
                        string += str(self._wordsCounter[file])
                else:
                    if self._args.chars:
                        string += str(self._charsCounter[file])
            string += "\t" + file
            logging.info(string)

        string = ""
        if self._args.lines:
            if self._args.words:
                if self._args.chars:
                    string += str(sum(self._linesCounter.values())) + "\t" + str(sum(self._wordsCounter.values())) + \
                              "\t" + str(sum(self._charsCounter.values()))
                else:
                    string += str(sum(self._linesCounter.values())) + "\t" + str(sum(self._wordsCounter.values()))
            else:
                if self._args.chars:
                    string += str(sum(self._linesCounter.values())) + "\t" \
                              + str(sum(self._charsCounter.values()))
                else:
                    string += str(sum(self._linesCounter.values()))
        else:
            if self._args.words:
                if self._args.chars:
                    string += str(sum(self._wordsCounter.values()) + "\t" + str(sum(self._charsCounter.values())))
                else:
                    string += str(sum(self._wordsCounter.values()))
            else:
                if self._args.chars:
                    string += str(sum(self._charsCounter.values()))
        string += "\ttotal"
        logging.info(string)


def main():
    parser = argparse.ArgumentParser(description="Word counter based on unix's wc command")
    parser.add_argument("input_files", nargs="+", help="name of input file")
    parser.add_argument("-c", "--chars", help="Count characters in selected files", action="store_true")
    parser.add_argument("-l", "--lines", help="Count lines in selected files", action="store_true")
    parser.add_argument("-w", "--words", help="Count words in selected files", action="store_true")
    args = parser.parse_args()

    word_counter = WordCounter(args)

    if args.lines:
        word_counter.count_lines_in_all_files()
    if args.words:
        word_counter.count_words_in_all_files()
    if args.chars:
        word_counter.count_chars_in_all_files()

    word_counter.print_logs_to_file()

if __name__ == '__main__':
    main()
