def is_power(a,b):
    """Returns True if a is a power of b and False otherwise."""
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False


if __name__ == '__main__':
    print(is_power(9,3))    # Returns True.
    print(is_power(12, 4))  # Returns False.
