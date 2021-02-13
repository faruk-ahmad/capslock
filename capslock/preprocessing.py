"""
This module introduces some classes for preprocessing text
data e.g. getting unique words, getting word frequency etc.

Author: Faruk Ahmad
Date: 13/02/2021
Email: faruk.csebrur@gmail.com
"""

import os

class Preprocessing:
    """This class defines preprocessing methods.
    Args:
        text: a path to text file or a string or a list of
        strings
    """
    def __init__(self, text, delim=' '):
        self.text = text
        self.delim = delim


    def _read_text(self):
        """
        -This private method iterate over lines if text
        is given as list of strings or file object.
        -Reads the text file and yield a line in each call
        """
        if isinstance(self.text, list):
            for txt in self.text:
                words = txt.split(sep=self.delim)
                for word in words:
                    yield word
        elif os.path.exists(self.text):
            with open(self.text) as lines:
                for line in lines:
                    words = line.split(sep=self.delim)
                    for word in words:
                        yield word
        elif isinstance(self.text, str):
            words = self.text.split(sep=self.delim)
            for word in words:
                yield word
    
    def get_unique_words(self):
        """This method returns unique words from a text
        data or text file.
        """
        unique_words = set()
        for word in self._read_text():
            unique_words.add(word)
        return list(unique_words)


if __name__ == '__main__':
    p = ['hello world', 'bangladesh is a riverin country']
    prep = Preprocessing(p)
    # prep._read_text()
    # for p in prep._read_text():
    #     print(p)
    uw = prep.get_unique_words()
    print(uw)