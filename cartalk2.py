"""
Exercise 9.8 from Think Python.
This exercise asks you to find a six digit number n with following props:
-last four digits of n are palindromic.
-last five digits of n + 1 are palindromic.
-middle four digits of n + 2 are palindromic.
-all digits of n + 3 are palindromic.

"""

def last_four_palindrome(n):
    """Returns True if last four digits of six digit number n are palindromic."""
    s = str(n)[2:]
    return s == s[::-1]


def last_five_palindrome(n):
    """Returns True if last five digits of six digit number n are palindromic."""
    s = str(n)[1:]
    return s == s[::-1]


def mid_four_palindrome(n):
    """Returns True if middle four digits of six digit number n are palindromic."""
    s = str(n)[1:5]
    return s == s[::-1]


def is_palindrome(n):
    """Returns True if number n is palindromic."""
    s = str(n)
    return s == s[::-1]


def find_all_solutions():
    """Finds all solutions to problem stated above."""
    return {n for n in range(100000, 1000000) if last_four_palindrome(n) and last_five_palindrome(n + 1) and mid_four_palindrome(n + 2) and is_palindrome(n + 3)}


def main():
    print(find_all_solutions())


if __name__ == '__main__':
    main()
