"""
Algorithm for finding non-empty continuous subarray with maximum sum. Time complexity: Θ(n).
Idea:
    Максимальный подмассив массива arr[:i+1] представляет собой либо максимальный подмассив массива arr[:i], либо
    подмассив arr[low:i+1], для некоторого 0 <= low <= i. Текущий подмассив arr[low:i+1] рассматривается, пока его 
    сумма (sm) больше 0, если же значение arr[i] привело sm в отрицательное значение, то рассматривается подмассив,
    начинающийся со следующего элемента (low = i + 1; sm = 0), так как если значение этого элемента будет положительным,
    то он гарантировано создаст единичный подмассив (из него самого) с локальной суммой большей, чем эта. Если же
    элемент x положителен и текущая сумму больше максимальной, то текущий подмассив arr[low:i+1] становится максимальным.
"""
from __future__ import annotations


def max_sum_subarray(arr: list) -> tuple[int, int, int]:
    """
    Examples:
        >>> max_sum_subarray([-1, -2, -3, -4, 0])
        (4, 4, 0)
        >>> max_sum_subarray([-4, -2, -1, -3])
        (2, 2, -1)
        >>> max_sum_subarray([-2, -5, 6, -2, -3, 1, 5, -6])
        (2, 6, 7)
        >>> max_sum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
        (7, 10, 43)
    """
    max_low = max_high = -1
    max_sum = float("-inf")
    low = sm = 0
    for i in range(len(arr)):
        sm += arr[i]
        if sm > max_sum:
            max_low = low
            max_high = i
            max_sum = sm
        elif sm < 0:
            sm = 0
            low = i + 1
    return max_low, max_high, max_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
