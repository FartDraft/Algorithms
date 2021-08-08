"""
Algorithm for solving Sudoku puzzles of any difficulty. It takes a sudoku grid and returns
a 9x9 array with the proper answer for the puzzle. Or it returns None in cases of:
    1. Invalid grid (not 9x9; values not in the range 1~9; digits in rows, columns or squares are repeated);
    2. Multiple solutions for the same puzzle or the puzzle is unsolvable.
"""
from typing import List, Optional
from collections import defaultdict


Matrix = List[List[int]]


def unique(line: List[int]) -> bool:
    """
    Examples:
        >>> unique(list(range(10)))
        True
        >>> unique([1, 4, 7, 5, 3, 1, 9, 2, 8])
        False
    """
    exist = defaultdict(bool)
    for dig in line:
        if exist[dig]:
            return False
        exist[dig] = True
    return True


def check(puzzle: Matrix) -> bool:
    if len(puzzle) != 9:
        return False
    count = 0
    for row in puzzle:
        if len(row) != 9:
            return False
        for dig in row:
            if not isinstance(dig, int) or not 0 <= dig <= 9:
                return False
            elif dig != 0:
                count += 1
    # The minimum number of open digits for an unique solution is 17.
    if count < 17:
        return False

    for row in puzzle:
        row = list(filter(bool, row))
        if not unique(row):
            return False
    for column in zip(*puzzle):
        column = list(filter(bool, list(column)))
        if not unique(column):
            return False
    for square in [[puzzle[3*r + rr][3*c + cc] for rr in range(3) for cc in range(3)]
                   for r in range(3) for c in range(3)]:
        square = list(filter(bool, square))
        if not unique(square):
            return False
    return True


def solve(puzzle: Matrix) -> Optional[Matrix]:
    min_allow = 10
    for row, col in [(r, c) for r in range(9) for c in range(9) if not puzzle[r][c]]:
        rr, cc = row // 3 * 3, col // 3 * 3
        use = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (
              {puzzle[r][col] for r in range(9)} | {puzzle[row][c] for c in range(9)} |
              {puzzle[rr + r][cc + c] for r in range(3) for c in range(3)})

        allow = len(use)
        if not allow:
            return
        if allow == 1:
            dig = use.pop()
            puzzle[row][col] = dig
            return solve(puzzle)
        if min_allow > allow:
            min_allow, min_use, min_row, min_col = allow, use, row, col

    if min_allow == 2:
        success = None
        for dig in min_use:
            replica = [row.copy() for row in puzzle]
            replica[min_row][min_col] = dig
            attempt = solve(replica)
            if attempt:
                if success:
                    return
                success = attempt
        return success
    if min_allow != 10:
        return
    return puzzle


def sudoku_puzzle(puzzle: Matrix) -> Optional[Matrix]:
    """
    Examples:
        >>> sudoku_puzzle([[1], [2], [3]])
       
        >>> sudoku_puzzle([[0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 0, 0, 0, 0]])

        >>> sudoku_puzzle([[1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ...                [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        
        >>> sudoku_puzzle([[1, 2, 3, 4, 5, 6, 7, 8, 'a'],
        ...                [4, 0, 6, 7, 8, 9, 1, 2, 3],
        ...                [7, 8, 9, 1, 2, 3, 4, 5, 6],
        ...                [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ...                [5, 6, 7, 8, 9, 1, 2, 3, 4],
        ...                [8, 9, 1, 2, 3, 4, 5, 6, 7],
        ...                [3, 4, 5, 6, 7, 8, 9, 1, 2],
        ...                [6, 7, 8, 9, 1, 2, 3, 4, 5],
        ...                [9, 1, 2, 3, 4, 5, 6, 7, 8]])

        >>> sudoku_puzzle([[0, 9, 6, 5, 0, 4, 0, 7, 1],
        ...                [0, 2, 0, 1, 0, 0, 0, 0, 0],
        ...                [0, 1, 4, 0, 9, 0, 6, 2, 3],
        ...                [0, 0, 3, 0, 6, 0, 0, 8, 0],
        ...                [0, 0, 8, 0, 5, 0, 4, 0, 0],
        ...                [9, 0, 0, 4, 1, 0, 0, 0, 5],
        ...                [7, 0, 0, 0, 0, 9, 0, 0, 0],
        ...                [0, 0, 1, 0, 7, 5, 3, 4, 9],
        ...                [2, 3, 0, 0, 4, 8, 1, 0, 7]])

        >>> sudoku_puzzle([[0, 0, 6, 1, 0, 0, 0, 0, 8],
        ...                [0, 8, 0, 0, 9, 0, 0, 3, 0],
        ...                [2, 0, 0, 0, 0, 5, 4, 0, 0],
        ...                [4, 0, 0, 0, 0, 1, 8, 0, 0],
        ...                [0, 3, 0, 0, 7, 0, 0, 4, 0],
        ...                [0, 0, 7, 9, 0, 0, 0, 0, 3],
        ...                [0, 0, 8, 4, 0, 0, 0, 0, 6],
        ...                [0, 2, 0, 0, 5, 0, 0, 8, 0],
        ...                [1, 0, 0, 0, 0, 2, 5, 0, 0]])  # doctest: +NORMALIZE_WHITESPACE
        [[3, 4, 6, 1, 2, 7, 9, 5, 8],
         [7, 8, 5, 6, 9, 4, 1, 3, 2],
         [2, 1, 9, 3, 8, 5, 4, 6, 7],
         [4, 6, 2, 5, 3, 1, 8, 7, 9],
         [9, 3, 1, 2, 7, 8, 6, 4, 5],
         [8, 5, 7, 9, 4, 6, 2, 1, 3],
         [5, 9, 8, 4, 1, 3, 7, 2, 6],
         [6, 2, 4, 7, 5, 9, 3, 8, 1],
         [1, 7, 3, 8, 6, 2, 5, 9, 4]]
        
        >>> sudoku_puzzle([[3, 0, 5, 0, 9, 0, 0, 0, 0],
        ...                [1, 0, 0, 0, 0, 0, 5, 4, 0],
        ...                [0, 0, 4, 6, 0, 0, 0, 0, 0],
        ...                [0, 0, 0, 2, 0, 0, 9, 0, 0],
        ...                [0, 6, 0, 4, 8, 9, 0, 1, 0],
        ...                [0, 0, 2, 0, 0, 5, 0, 0, 0],
        ...                [0, 0, 0, 0, 0, 8, 1, 0, 0],
        ...                [0, 8, 1, 0, 0, 0, 0, 0, 2],
        ...                [0, 0, 0, 0, 7, 0, 3, 0, 8]])  # doctest: +NORMALIZE_WHITESPACE
        [[3, 2, 5, 7, 9, 4, 8, 6, 1],
         [1, 7, 6, 8, 3, 2, 5, 4, 9],
         [8, 9, 4, 6, 5, 1, 7, 2, 3],
         [4, 5, 8, 2, 1, 7, 9, 3, 6],
         [7, 6, 3, 4, 8, 9, 2, 1, 5],
         [9, 1, 2, 3, 6, 5, 4, 8, 7],
         [6, 3, 7, 5, 2, 8, 1, 9, 4],
         [5, 8, 1, 9, 4, 3, 6, 7, 2], 
         [2, 4, 9, 1, 7, 6, 3, 5, 8]]
    """
    if not check(puzzle):
        return
    return solve(puzzle)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
