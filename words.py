

def get_word_set():
    f = open('/home/john/Desktop/python_stuff/words.txt')
    word_set = set([])
    for line in f:
        word_set.add(line.strip())
    return word_set
