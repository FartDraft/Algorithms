"""
Recursive algorithm for finding non-empty continuous subarray with maximum sum.
Divine and Conquer paradigm. Time complexity: Θ(n log n).
There is a solution in Θ(n). Find max_sum_subarray.
Idea:
    mid - средняя точка массива arr[low:high+1]. Заметим, что максимальный непрерывный
    подмассив arr[i:j+1] массива arr[low:high+1] находиться только в одном из следующих положений:
        1. Полностью располагается в подмассиве arr[low:mid+1], так что low <= i <= j <= mid;
        2. Полностью располагается в подмассиве arr[mid+1:high+1], так что mid < i <= j <= high;
        3. Пересекает среднюю точку, так что low <= i <= mid < j <= high.
    Следовательно, максимальный подмассив массива arr[low:high+1] должен иметь наибольшую сумму
    среди всех подмассивов из каждого положения. Максимальные подмассивы arr[low:mid+1] и
    arr[mid+1:high+1] находим рекурсивно. Максимальный подмассив, пересекающий среднюю точку
    находим с помощью функции max_sum_crossing_subarray за время Θ(N).
"""
from __future__ import annotations


def max_sum_crossing_subarray(arr: list, low: int, mid: int, high: int) -> tuple[int, int, int]:
    """
    Idea:
        Любой подмассив arr[i:j+1], пересекающий среднюю точку (mid), состоит из двух подмассивов
        arr[i:mid+1] и arr[mid+1:j+1], где low <= i <= mid < j <= high. Следовательно, находим
        максимальные непрерывные подмассивы arr[i:mid+1] (левая половина) и
        arr[mid+1:j+1] (правая половина), а затем объединяем их.
    """
    max_left = max_right = mid
    left_sum = right_sum = float("-inf")
    # Левая половина.
    sm = 0
    for i in range(mid, low - 1, -1):
        sm += arr[i]
        if sm > left_sum:
            left_sum = sm
            max_left = i
    # Правая половина.
    sm = 0
    for i in range(mid + 1, high + 1):
        sm += arr[i]
        if sm > right_sum:
            right_sum = sm
            max_right = i
    # Объединение.
    return max_left, max_right, left_sum + right_sum


def _recursive_max_sum_subarray(arr: list, low: int, high: int) -> tuple[int, int, int]:
    # Базовый случай.
    if low == high:
        return low, high, arr[low]
    # Рекурсивный случай. Разделение.
    mid = (high + low) // 2
    # Властвование.
    left_low, left_high, left_sum = _recursive_max_sum_subarray(arr, low, mid)
    right_low, right_high, right_sum = _recursive_max_sum_subarray(arr, mid + 1, high)
    # Комбинирование.
    cross_low, cross_high, cross_sum = max_sum_crossing_subarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif cross_sum >= left_sum and cross_sum >= right_sum:
        return cross_low, cross_high, cross_sum
    return right_low, right_high, right_sum


def recursive_max_sum_subarray(arr: list) -> tuple[int, int, int]:
    """
    Examples:
        >>> recursive_max_sum_subarray([-1, -2, -3, -4, 0])
        (4, 4, 0)
        >>> recursive_max_sum_subarray([-4, -2, -1, -3])
        (2, 2, -1)
        >>> recursive_max_sum_subarray([-2, -5, 6, -2, -3, 1, 5, -6])
        (2, 6, 7)
        >>> recursive_max_sum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
        (7, 10, 43)
    """
    return _recursive_max_sum_subarray(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
