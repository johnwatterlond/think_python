
def gcd(a,b):
    """
    Return the GCD of a and b.
    """
    return a if b == 0 else gcd(b, a % b)



if __name__ == '__main__':
    print(gcd(3, 6))
    print(gcd(3, 100))
