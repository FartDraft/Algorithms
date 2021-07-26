"""
Pure Python implementation of the merge sort algorithm.
Merge sort is an efficient, general-purpose, and comparison-based sorting algorithm.
Divine and Conquer paradigm. Time complexity: Θ(n log n).
Idea:
    Разделение:
        Делим массив arr на 2 подмассива длиной len(arr) / 2.
    Властвование:
        Рекурсивно сортируем эти 2 подмассива с использованием сортировки слиянием.
    Комбинирование:
        Сливаем такие два подмассива с помощью функции merge для получения окончательного
        отсортированного ответа.
"""


def merge(left: list, right: list) -> list:
    """
    Examples:
        >>> merge([], [])
        []
        >>> merge([0, 2, 5], [2, 3])
        [0, 2, 2, 3, 5]
        >>> merge([-5, -2], [-45, 5])
        [-45, -5, -2, 5]
        >>> merge(['ad', 'mer', 'ze'], ['an', 'g', 'zip'])
        ['ad', 'an', 'g', 'mer', 'ze', 'zip']
        >>> merge(['17', '4', 'm'], ['2', 'da', 'ye'])
        ['17', '2', '4', 'da', 'm', 'ye']
    """
    def _merge():
        while left and right:
            yield (left if left[0] <= right[0] else right).pop(0)
        yield from left
        yield from right

    return list(_merge())



def merge_sort(arr: list) -> list:
    """
    Examples:
        >>> merge_sort([])
        []
        >>> merge_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> merge_sort([-2, 5, -5, -45])
        [-45, -5, -2, 5]
        >>> merge_sort(['an', 'zip', 'ad', 'mer', 'g', 'ze'])
        ['ad', 'an', 'g', 'mer', 'ze', 'zip']
        >>> merge_sort(['4', 'm', 'ye', 'da', '2', '17'])
        ['17', '2', '4', 'da', 'm', 'ye']
    """

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
