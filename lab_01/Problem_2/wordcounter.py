from os.path import isfile
import logging
import re

class WordCounter():
    @staticmethod
    def Count(file_to_parse):
        if isfile(file_to_parse):
            with open(file_to_parse) as file:
                array3 = []
                array2 = []
                for line in file:
                    array = line.split(" ")
                    array = [x for x in array if len(x) > 0 and re.match("[A-Za-z]+", x)]
                    array2 = array2 + array
                for word in array2:
                    if (word, array2.count(word)) not in array3:
                        array3.append((word, array2.count(word)))
                array3.sort(key=lambda x: x[1])
                print(array3)
                with open("log.log".format(file_to_parse), "w") as log:
                    log.write('\n'.join('%s %s' % x for x in array3))
