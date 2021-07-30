"""
Selection sort is a simple sorting algorithm. Time complexity: Θ(n ** 2).
Idea:
    Алгоритм делит входной массив на две части: отсортированный подмассив элементов, который
    создается слева направо в начале массива, и подмассив оставшихся несортированных элементов,
    который занимает остальную часть массива. Изначально, отсортированный подмассив
    пуст, а несортированный подмассив представляет собой весь входной массив. Алгоритм выполняется
    путём нахождения наименьшего элемента в несортированном части массива, перестановки его с
    крайним левым несортированным элементом (помещая его в отсортированном порядке) и перемещения
    границы отсортированного подсписка на один элемент вправо.
"""


def selection_sort(arr: list) -> list:
    """
    Examples:
        >>> selection_sort([])
        []
        >>> selection_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> selection_sort([-2, 5, -5, -45])
        [-45, -5, -2, 5]
        >>> selection_sort(['an', 'zip', 'ad', 'mer', 'g', 'ze'])
        ['ad', 'an', 'g', 'mer', 'ze', 'zip']
        >>> selection_sort(['4', 'm', 'ye', 'da', '2', '17'])
        ['17', '2', '4', 'da', 'm', 'ye']
        >>> import random
        >>> arr = random.sample(range(-50, 50), 100)
        >>> selection_sort(arr) == sorted(arr)
        True
        >>> import string
        >>> arr = random.choices(string.ascii_letters + string.digits, k=100)
        >>> selection_sort(arr) == sorted(arr)
        True
    """
    arr = arr.copy()
    length = len(arr)
    for pos in range(length - 1):
        least = min(range(pos, length), key=arr.__getitem__)
        arr[pos], arr[least] = arr[least], arr[pos]
    return arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
