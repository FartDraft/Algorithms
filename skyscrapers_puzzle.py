"""
Algorithm for solving Skyscrapers puzzles of any size.
In a grid of size by size you want to place a skyscraper in each square with only some clues:
    1. The height of the skyscrapers is between 1 and size;
    2. No two skyscrapers in a row or column may have the same number of floors;
    3. A clue is the number of skyscrapers that you can see in a row or column from the outside;
    4. Higher skyscrapers block the view of lower skyscrapers located behind them.
It returns a size×size array with the proper answer for the puzzle. Or it returns None in cases of:
    1. Invalid view (not 9x9; values not in the range 1~9);
    2. Multiple solutions for the same puzzle or the puzzle is unsolvable.
"""
from typing import List, Tuple, Optional
from itertools import permutations, product


Matrix = List[List[int]]


def check(view: Tuple[int], size: int) -> bool:
    if len(view) != 4 * size:
        return False
    for clue in view:
        if not isinstance(clue, int) or not 0 <= clue <= size:
            return False
    return True


def solve(view: Tuple[int], size: int) -> Optional[Matrix]:
    rg0, rg1 = range(size), range(1, size + 1)
    # Словарь всех возможных перестановок размеров небоскрёбов для каждого видения.
    variants = {key: set() for key in range(size + 1)}
    for variant in permutations(rg1):
        maximum = vision = 0
        for dig in variant:
            if dig > maximum:
                maximum = dig
                vision += 1
        variants[0].add(variant)
        variants[vision].add(variant)

    # Фильтрация по подсказкам. Горизонтальное (hor) и вертикальное (ver) представления пазла.
    hor = [variants[r] & {variant[::-1] for variant in variants[l]}
           for (r, l) in zip(view[4*size - 1: 3*size - 1: -1], view[size: 2*size])]
    ver = [variants[t] & {variant[::-1] for variant in variants[b]}
           for (t, b) in zip(view[0: size], view[3*size - 1: 2*size - 1: -1])]

    # Фильтрация по совместимости строк и колонн.
    check = 0  # Общее количество вариантов линий горизонтального и вертикального представлений.
    memory = -1  # Значение check на предыдущей итерации цикла.

    # check = 2*size <—> в обоих представлениях осталось по одному варианту на каждую линию.
    # check = memory <—> не было и более не будет отфильтровано ни одного варианта.
    while check != 2*size and check != memory:
        for i, j in product(rg0, rg0):
            common = {line[j] for line in hor[i]} & {line[i] for line in ver[j]}
            hor[i] = [line for line in hor[i] if line[j] in common]
            ver[j] = [line for line in ver[j] if line[i] in common]
        memory, check = check, sum(len(line_variants) for line_variants in hor + ver)

    # Перебор оставшихся вариантов.
    valid = {*rg1}
    success = None
    for puzzle_variant in product(*hor):
        # Если каждый столбец представляет собой множество чисел от 1 до size включительно.
        if all({puzzle_variant[i][j] for i in rg0} == valid for j in rg0):
            if success:  # Если вариантов решения пазла множество.
                return
            success = list(list(row) for row in puzzle_variant)
    return success


def skyscrapers_puzzle(view: Tuple[int], size: int) -> Optional[Matrix]:
    """
    Examples:
        >>> skyscrapers_puzzle((2, 2, 1, 3,  2, 2, 3, 1,  1, 2, 2, 3,  3, 2, 1, 3), 5)
        
        >>> skyscrapers_puzzle((2, 2, 1, 3,  2, 2, 3, 1,  5, 2, 2, 3,  3, 2, 1, 3), 4)
        
        >>> skyscrapers_puzzle((2, 2, 1, 3,  2, 2, 3, 1,  'a', 2, 2, 3,  3, 2, 1, 3), 4) 
        
        >>> skyscrapers_puzzle((2, 1, 3, 2,  3, 2, 1, 2,  2, 1, 2, 3,  2, 3, 1, 2), 4)
        
        >>> skyscrapers_puzzle((1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1), 4)

        >>> skyscrapers_puzzle((), 0)
        []

        >>> skyscrapers_puzzle((1,  1,  1,  1), 1)
        [[1]]
        
        >>> skyscrapers_puzzle((1, 2,  2, 1,  1, 2,  2, 1), 2)
        [[2, 1], [1, 2]]

        >>> skyscrapers_puzzle((3, 1, 2,  2, 1, 3,  2, 2, 1,  1, 2, 2), 3)
        [[1, 3, 2], [2, 1, 3], [3, 2, 1]]
        
        >>> skyscrapers_puzzle((0, 0, 1, 2,  0, 2, 0, 0,  0, 3, 0, 0,  0, 1, 0, 0), 4)
        [[2, 1, 4, 3], [3, 4, 1, 2], [4, 2, 3, 1], [1, 3, 2, 4]]
        
        >>> skyscrapers_puzzle((2, 0, 0, 2, 4,  4, 0, 2, 3, 0,  0, 0, 2, 3, 0,  4, 0, 4, 0, 0), 5)
        [[3, 5, 4, 2, 1], [5, 4, 2, 1, 3], [1, 2, 3, 5, 4], [4, 1, 5, 3, 2], [2, 3, 1, 4, 5]]
        
        >>> skyscrapers_puzzle((0, 3, 0, 5, 3, 4,  0, 0, 0, 0, 0, 1,
        ...                     0, 3, 0, 3, 2, 3,  3, 2, 0, 3, 1, 0), 6)  # doctest: +NORMALIZE_WHITESPACE
        [[5, 2, 6, 1, 4, 3], [6, 4, 3, 2, 5, 1], [3, 1, 5, 4, 6, 2],
         [2, 6, 1, 5, 3, 4], [4, 3, 2, 6, 1, 5], [1, 5, 4, 3, 2, 6]]
        >>> skyscrapers_puzzle((0, 2, 3, 0, 2, 0, 0,  5, 0, 4, 5, 0, 4, 0,
        ...                     0, 4, 2, 0, 0, 0, 6,  0, 0, 0, 0, 0, 0, 0), 7)  # doctest: +NORMALIZE_WHITESPACE
        [[7, 6, 2, 1, 5, 4, 3], [1, 3, 5, 4, 2, 7, 6], [6, 5, 4, 7, 3, 2, 1], [5, 1, 7, 6, 4, 3, 2],
         [4, 2, 1, 3, 7, 6, 5], [3, 7, 6, 2, 1, 5, 4], [2, 4, 3, 5, 6, 1, 7]] 
    """
    if not check(view, size):
        return
    return solve(view, size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
