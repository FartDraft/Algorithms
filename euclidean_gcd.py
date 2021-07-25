def euclidean_gcd(a: int, b: int) -> int:
    """Algorithm for finding the largest common divisor of a and b.
    
    Examples:
        >>> euclidean_gcd(3, 5)
        1
        >>> euclidean_gcd(6, 3)
        3
        >>> euclidean_gcd(2261, 4199)
        323
    """
    return a if b == 0 else euclidean_gcd(b, a % b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
