"""
Strassen algorithm for matrix multiplication. Time complexity: Θ(N ** log 7).
It supports only square matrices of length equal to degree 2.
"""
from __future__ import annotations


def default_matrix_multiplication(a: list, b: list) -> list:
    """Multiply only for 2x2 matrices."""
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


def matrix_addition(a: list, b: list) -> list:
    return [[a[row][col] + b[row][col] for col in range(len(a[row]))] for row in range(len(a))]


def matrix_subtraction(a: list, b: list) -> list:
    return [[a[row][col] - b[row][col] for col in range(len(a[row]))] for row in range(len(a))]


def matrix_dimensions(matrix: list) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


def matrix_split(matrix: list) -> tuple[list, list, list, list]:
    """
    Examples:
        >>> matrix_split([[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]])
        ([[4, 3], [2, 3]], [[2, 4], [1, 1]], [[6, 5], [8, 4]], [[4, 3], [1, 6]])
        >>> matrix_split([
        ...     [4, 3, 2, 4,  4, 3, 2, 4], [2, 3, 1, 1,  2, 3, 1, 1],
        ...     [6, 5, 4, 3,  6, 5, 4, 3], [8, 4, 1, 6,  8, 4, 1, 6],
        ...     [4, 3, 2, 4,  4, 3, 2, 4], [2, 3, 1, 1,  2, 3, 1, 1],
        ...     [6, 5, 4, 3,  6, 5, 4, 3], [8, 4, 1, 6,  8, 4, 1, 6]
        ... ])  # doctest: +NORMALIZE_WHITESPACE
        ([[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
         [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
         [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
         [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]])
    """
    matrix_length = len(matrix)
    mid = matrix_length >> 1

    return (
        [[matrix[i][j] for j in range(mid)] for i in range(mid)],
        [[matrix[i][j] for j in range(mid, matrix_length)] for i in range(mid)],
        [[matrix[i][j] for j in range(mid)] for i in range(mid, matrix_length)],
        [[matrix[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]
    )


def combine_parts(top_left: list, top_right: list, bot_left: list, bot_right: list) -> list:
    """
    Examples:
        >>> combine_parts([[4, 3], [2, 3]], [[2, 4], [1, 1]], [[6, 5], [8, 4]], [[4, 3], [1, 6]])
        [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]]
        >>> combine_parts(
        ...     [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        ...     [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        ...     [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        ...     [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]]
        ... )  # doctest: +NORMALIZE_WHITESPACE
        [[4, 3, 2, 4, 4, 3, 2, 4], [2, 3, 1, 1, 2, 3, 1, 1],
         [6, 5, 4, 3, 6, 5, 4, 3], [8, 4, 1, 6, 8, 4, 1, 6],
         [4, 3, 2, 4, 4, 3, 2, 4], [2, 3, 1, 1, 2, 3, 1, 1],
         [6, 5, 4, 3, 6, 5, 4, 3], [8, 4, 1, 6, 8, 4, 1, 6]]
        
    """
    matrix_length = len(top_left)

    matrix = [[0 for _ in range(matrix_length << 1)] for _ in range(matrix_length << 1)]
    for i in range(matrix_length):
        for j in range(matrix_length):
            matrix[i][j] = top_left[i][j]
            matrix[i][matrix_length + j] = top_right[i][j]
            matrix[matrix_length + i][j] = bot_left[i][j]
            matrix[matrix_length + i][matrix_length + j] = bot_right[i][j]
    return matrix


def strassen_matrix_multiplication(a: list, b: list) -> list:
    """
    Examples:
        >>> strassen_matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> strassen_matrix_multiplication(
        ...     [[6, 2, 2, 4], [5, 1, 1, 8], [7, 5, 4, 8], [1, 6, 4, 8]],
        ...     [[8, 1, 8, 6], [5, 6, 7, 1], [2, 5, 6, 1], [4, 8, 2, 6]]
        ... )  # doctest: +NORMALIZE_WHITESPACE
        [[78, 60, 82, 64], [79, 80, 69, 80], [121, 121, 131, 99], [78, 121, 90, 64]]
    """
    if matrix_dimensions(a) == (2, 2):
        return default_matrix_multiplication(a, b)

    atl, atp, abl, abr = matrix_split(a)
    btl, btp, bbl, bbr = matrix_split(b)

    t1 = strassen_matrix_multiplication(atl, matrix_subtraction(btp, bbr))
    t2 = strassen_matrix_multiplication(matrix_addition(atl, atp), bbr)
    t3 = strassen_matrix_multiplication(matrix_addition(abl, abr), btl)
    t4 = strassen_matrix_multiplication(abr, matrix_subtraction(bbl, btl))
    t5 = strassen_matrix_multiplication(matrix_addition(atl, abr), matrix_addition(btl, bbr))
    t6 = strassen_matrix_multiplication(matrix_subtraction(atp, abr), matrix_addition(bbl, bbr))
    t7 = strassen_matrix_multiplication(matrix_subtraction(atl, abl), matrix_addition(btl, btp))

    return combine_parts(matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2), t6),
                         matrix_addition(t1, t2), matrix_addition(t3, t4),
                         matrix_subtraction(matrix_subtraction(matrix_addition(t1, t5), t3), t7))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
