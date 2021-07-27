"""
Algorithm for finding the number of inversions in array.
Divine and Conquer paradigm. Time complexity: Θ(n log n).
Idea:
    Если arr[i] > arr[j] и i < j, то пара (i, j) называется инверсией массива arr.
    Модифицируем сортировку слиянием. В функции слияния есть такой шаг, когда текущий элемент
    левой части больше текущего элемента правой части. Вот в этот момент нужно к (локальному)
    счётчику инверсий (invcount) добавить количество ещё неиспользованных элементов левой 
    половины. А непосредственно в функции сортировки слиянием необходимо сложить количество
    инверсий в левой половине, количество в правой, и количество инверсий, возникающих при
    слиянии этих частей.
"""


def modified_merge(arr: list, s: int, m: int, e: int) -> int:
    left = arr[s: m]
    right = arr[m: e + 1]
    len_left, len_right = len(left), len(right)
    i = j = invcount = 0
    k = s
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            invcount += len_left - i
        k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1
            
    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1
    return invcount


def modified_merge_sort(arr: list, s: int, e: int) -> int:
    if s < e:
        m = (s + e + 1) // 2
        return (modified_merge_sort(arr, s, m - 1) + modified_merge_sort(arr, m, e) + 
                modified_merge(arr, s, m, e))
    return 0


def inversions_num(arr: list) -> int:
    """
    Examples:
        >>> inversions_num([])
        0
        >>> inversions_num([0, 5, 3, 2, 2])
        5
        >>> inversions_num([-2, 5, -5, -45])
        5
        >>> inversions_num(['an', 'zip', 'ad', 'mer', 'g', 'ze'])
        6
        >>> inversions_num(['4', 'm', 'ye', 'da', '2', '17'])
        11
        >>> inversions_num([5, 2, 1, 7, 3, 2, 1])
        13
    """
    arr_copy = arr.copy()
    return modified_merge_sort(arr_copy, 0, len(arr) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
