"""
These are solutions to exercises from think python from section 9.2.

"""

from words import word_set


def words_len_greater_than(n):
	"""Find words in word_set that have length greater than n."""
	return {w for w in word_set if len(w) > n}


def has_no_letter(w, l):
	return not l in w


def words_without_letter(l):
	"""Finds all words in word_set that do not have the letter l."""
	return {w for w in word_set if has_no_letter(w, l)}


def percent_without_letter(l):
	"""Finds percentage of words in word_set without letter l."""
	return len(words_without_letter(l)) / len(word_set)


def avoids(w, forbidden):
	"""Checks if word w doesn't contain letters from forbidden."""
	return set(w).isdisjoint(set(forbidden))


def user_avoid_count():
	"""
	Prints number of words from word_set that avoid
	the user submitted string of letters.

	"""
	forbidden = input('Enter a string of forbidden letters.\n> ')
	print(len({w for w in word_set if avoids(w, forbidden)}))


def uses_only(w, letters):
	"""Checks if word w is made from letters."""
	return set(w).issubset(set(letters))


def words_uses_only(letters):
	"""Finds all words in word_set made from letters."""
	return {w for w in word_set if uses_only(w, letters)}


def uses_all(w, letters):
	"""Checks if word w contains all letters in letters."""
	return set(letters).issubset(set(w))


def is_abecedarian(w):
	"""Checks if letters in word w appear in alphabetical order."""
	return list(w) == sorted(list(w))
