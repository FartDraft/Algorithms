"""
Given an array of integers (arr) and an integer (m), returns
the sum of the product of its subsequences of length m.
Explanation for subsequence_product_sum(arr=[2, 3, 4, 5, 6], m=3):
    Must return:
        2*3*4 + 2*3*5 + 2*3*6 + 2*4*5 + 2*4*6 + 2*5*6 + 3*4*5 + 3*4*6 + 3*5*6 + 4*5*6 = 580
    num =
        2 -> lengths = [1, 2, 0, 0]
        3 -> lengths = [1, 2+3, 2*3, 0]
        4 -> lengths = [1, 5+4, 6 + 5*4, 6*4]
        5 -> lengths = [1, 9+5, 26 + 9*5, 24 + 26*5]
        6 -> lengths = [1, 14+6, 71 + 14*6, 154 + 71*6]
    lengths contains sums of subsequences of length from 0 to m (inclusive). The sum of
    a subsequence of length 0 equals 1.
"""


def subsequence_product_sum(arr: list, m: int) -> int:
    """
    Examples:
        >>> subsequence_product_sum([2, 3, 4, 5, 6], 0)
        1
        >>> subsequence_product_sum([2, 3, 4, 5, 6], 1)
        20
        >>> subsequence_product_sum([2, 3, 4, 5, 6], 2)
        155
        >>> subsequence_product_sum([2, 3, 4, 5, 6], 3)
        580
        >>> subsequence_product_sum([6,7,8,5,2,4,9,3,1,10], 6)
        3416930
        >>> subsequence_product_sum([3, 10, 7, 9, 1, 4, 5, 2, 8, 6], 7)
        8409500
        >>> subsequence_product_sum([7,9,4,2,3,10,8,6,5,1], 9)
        10628640
        >>> subsequence_product_sum([10,7,8,5,6,9,4,1,2,3], 8)
        12753576
    """
    lengths = [1] + m*[0]
    for num in arr:
        for i in range(m, 0, -1):
            lengths[i] += lengths[i - 1] * num
    return lengths[m]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
