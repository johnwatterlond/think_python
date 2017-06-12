"""
Exercise 9.7 from Think Python.
This exercise asks you to find a word with three consecutive double letters.

"""

from words import word_set


def has_three_cons_doubs(w):
	"""Returns True if word w has three consecutive double letters."""
	for i in range(len(w)-5):
		if w[i]==w[i+1] and w[i+2]==w[i+3] and w[i+4]==w[i+5]:
			return True
	return False


def find_three_cons_doubs():
	return {w for w in word_set if has_three_cons_doubs(w)}


def main():
	print(find_three_cons_doubs())


if __name__ == '__main__':
	main()
