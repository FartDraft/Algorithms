"""
Insertion sort is a simple sorting algorithm. Time complexity: Θ(n ** 2).
Idea:
    Сортировка вставкой напоминает способ, к которому прибегают игроки для сортировки имеющихся на
    руках карт. Пусть вначале в левой руке (arr[:insert_index+1]) нет ни одной карты и все они
    лежат на столе рубашкой вверх. Далее со стола берётся по одной карте (insert_value), каждая из
    которых помещается в нужное место среди карт левой руки. Чтобы определить, куда нужно поместить
    очередную карту, её масть и достоинство сравниваются с мастью и достоинством карт в руке. В
    любой момент (в начале каждой итерации главного цикла) карты в левой руке будут
    остортированы, и это будут те карты, которые первоначально лежали в стопке на столе.
"""


def insertion_sort(arr: list) -> list:
    """
    Examples:
        >>> insertion_sort([])
        []
        >>> insertion_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> insertion_sort([-2, 5, -5, -45])
        [-45, -5, -2, 5]
        >>> insertion_sort(['an', 'zip', 'ad', 'mer', 'g', 'ze'])
        ['ad', 'an', 'g', 'mer', 'ze', 'zip']
        >>> insertion_sort(['4', 'm', 'ye', 'da', '2', '17'])
        ['17', '2', '4', 'da', 'm', 'ye']
        >>> import random
        >>> arr = random.sample(range(-50, 50), 100)
        >>> insertion_sort(arr) == sorted(arr)
        True
        >>> import string
        >>> arr = random.choices(string.ascii_letters + string.digits, k=100)
        >>> insertion_sort(arr) == sorted(arr)
        True
    """
    arr = arr.copy()
    for insert_index, insert_value in enumerate(arr[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < arr[insert_index]:
            arr[insert_index + 1] = arr[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            arr[insert_index + 1] = insert_value
    return arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
