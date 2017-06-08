"""
Two words interlock if taking alterlating letters from each
    forms a new word.
This exercise asks to find all pairs of words that interlock.

"""


from words import word_set
import pprint


def is_interlock(w, word_set):
    """Is word w formed by interlocking two words from word_set."""
    w1 = w[::2]
    w2 = w[1::2]
    return w1 in word_set and w2 in word_set


def find_interlocks(word_set):
    """Find all interlocking words from word_set."""
    return [[w, w[::2], w[1::2]] for w in word_set if is_interlock(w, word_set)]


def main():
    pprint.pprint(find_interlocks(word_set))


if __name__ == '__main__':
    main()
