"""
Binary search is a search algorithm that finds the position of a target value
within a sorted array. Time complexity: Θ(log n). Return index of found
item or None if item is not found.
Идея:
    Интервал поиска (от left до right включительно) при каждой итерации главного цикла
    уменьшается вдвое. Определяется средняя точка интервала поиска - mid. Пользуемся
    тем фактом, что массив отсортирован по возрастанию. Таким образом, если средний
    элемент (sorted_arr[mid]) меньше искомого (item), то ставим левую границу указывать на
    индекс mid+1, иначе ставим правую границу на mid (учитываем, что sorted_arr[mid] может
    быть равен item). Дожидаемся схождения левой и правой границ и сравниваем элемент на
    месте остановки правой границы (именно она отвечает за  местонахождение элемента x) с искомым.
"""


def binary_search(sorted_arr: list, item):
    """
    Examples:
        >>> binary_search([0, 2, 2, 3, 5], 2)
        1
        >>> binary_search([-45, -5, -2, 5], -5)
        1
        >>> binary_search(['ad', 'an', 'g', 'mer', 'ze', 'zip'], 'mer')
        3
        >>> binary_search(['17', '2', '4', 'da', 'm', 'ye'], '2')
        1
        >>> binary_search([i for i in range(1000)], 5)
        5
    """
    left, right = 0, len(sorted_arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if item > sorted_arr[mid]:
            left = mid + 1
        else:
            right = mid
    if sorted_arr[right] == item:
        return right
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
