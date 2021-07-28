"""
Bubble sort is a simple sorting algorithm. Time complexity: Θ(n ** 2).
Idea:
    Алгоритм состоит из повторяющихся проходов по сортируемому массиву. За каждый проход элементы
    последовательно сравниваются попарно и, если порядок в паре неверный, выполняется перестановка
    элементов. Проходы по массиву повторяются n-1 раз или до тех пор, пока на очередном проходе
    не окажется, что обмены больше не нужны, что означает — массив отсортирован. При каждом проходе
    алгоритма по внутреннему циклу, очередной наибольший элемент массива ставится на своё
    место в конце массива рядом с предыдущим «наибольшим элементом», а наименьший элемент
    перемещается на одну позицию к началу массива («всплывает» до нужной позиции, как пузырёк
    в воде — отсюда и название алгоритма).
"""


def bubble_sort(arr):
    """
    Examples:
        >>> bubble_sort([])
        []
        >>> bubble_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> bubble_sort([-2, 5, -5, -45])
        [-45, -5, -2, 5]
        >>> bubble_sort(['an', 'zip', 'ad', 'mer', 'g', 'ze'])
        ['ad', 'an', 'g', 'mer', 'ze', 'zip']
        >>> bubble_sort(['4', 'm', 'ye', 'da', '2', '17'])
        ['17', '2', '4', 'da', 'm', 'ye']
        >>> import random
        >>> arr = random.sample(range(-50, 50), 100)
        >>> bubble_sort(arr) == sorted(arr)
        True
        >>> import string
        >>> arr = random.choices(string.ascii_letters + string.digits, k=100)
        >>> bubble_sort(arr) == sorted(arr)
        True
    """
    length = len(arr)
    for i in range(length - 1):
        no_swap = True
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                no_swap = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if no_swap:
            break
    return arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
