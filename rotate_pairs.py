"""
Two words are rotate pairs if you can rotate one of them and get the other.
This exercise asks to find all rotate pairs.

"""

from words import word_set


def rotate_letter(l, n):
    """Shift/Rotate the letter l by integer n."""
    return chr(((ord(l) - ord('a') + n) % 26) + ord('a'))


def rotate_word(w, n):
    """Shift/Rotate entire word w by integer n."""
    letters = list(w)
    for i in range(len(w)):
        letters[i] = rotate_letter(letters[i], n)
    return ''.join(letters)


def find_rotate_pairs(w):
    """Find all rotate pairs for given word w."""
    s = set([])
    for n in range(26):
        if rotate_word(w, n) in word_set:
            s.add(rotate_word(w, n))
    return tuple(s)


def find_all_rotates():
    """Finds all rotate pairs for every word in word_set."""
    s1 = set([])  # tracking words seen.
    s2 = set([])  # actual rotate pairs.
    for w in word_set:
        if w not in s1:
            rots = find_rotate_pairs(w)
            for w1 in rots:
                s1.add(w1)
            if len(rots) > 1:
                s2.add(rots)
    return s2


def main():
    print(find_all_rotates())


if __name__ == '__main__':
    main()
