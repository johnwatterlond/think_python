"""
Program to generalize exercise 3.3 from think_python.

Example result for boxes(1):
+-----+
|     |
|     |
+-----+
"""



def plus_line(n):
    """If n=1, returns '+-----+', if n=2 returns '+-----+-----+'."""
    l = '{0}{0:->6}'.format('+') * n
    return l.replace('++', '+')

def minus_line(n):
    """If n=1, returns '|     |', if n=2 returns '|     |     |'."""
    l = '{0}{0:>6}'.format('|') * n
    return l.replace('||', '|')

def boxes(n):
    """Returns an n x n grid of boxes using plus_line and minus_line"""
    seq = [plus_line, minus_line, minus_line]
    for i in range(n):
        for f in seq:
            print(f(n))
    print(plus_line(n))
