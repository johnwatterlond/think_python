"""
To use:
from words import word_set

"""


def get_word_set():
    """Return set of words from think_python dictionary."""
    f = open('/home/john/Desktop/python_stuff/think_python/words.txt')
    word_set = set([])
    for line in f:
        word_set.add(line.strip())
    return word_set

word_set = get_word_set()
