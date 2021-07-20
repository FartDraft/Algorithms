def gcd(a: int, b: int) -> int:
    """Algorithm for finding the largest common divisor of a and b.
    
    Examples:
        >>> gcd(3, 5)
        1
        >>> gcd(6, 3)
        3
    """
    return a if b == 0 else gcd(b, a % b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
