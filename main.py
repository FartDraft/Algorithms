__author__ = "Afanasin Egor"
# При нахождении ошибки в работе функции или неточности в документации обращаться по почте:
__email__ = "fartdraft@gmail.com"


from math import trunc, sqrt
from random import choice


def is_simple(num: int) -> bool:
    """Проверка числа num на простоту.

    Args:
        num (int): натуральное число.

    Returns:
        bool: True - если число num простое, иначе False.
    """
    if num < 2 or not num % 2 or not num % 3:
        return False
    for k in range(6, trunc(sqrt(num)) + 2, 6):
        if not num % (k - 1) or not num % (k + 1):
            return False
    return True


def sieve(n: int) -> list:
    """Решето Эратосфена. Алгоритм проверки чисел на простоту до заданного 
        натурального числа (включительно) путём постепенного отсеивания составных чисел.

    Args:
        n (int):  натуральное число, включительно до которого будут проверены на простоту.

    Returns:
        list: массив bool значений. 
            Каждый индекс соответствует числу. True - если число простое, иначе - False.
    """
    assert n > 2, "n меньше чем 2"
    ret = [False, False] + [True] * (n - 1)
    for k in (2, 3):
        for i in range(k * k, n + 1, k):
            ret[i] = False
    for m in range(6, trunc(sqrt(n)) + 2, 6):
        for k in (m - 1, m + 1): 
            if ret[k]:
                for i in range(k * k, n + 1, k):
                    ret[i] = False
    return [i for i, x in enumerate(ret) if x]


def insertion_sort(arr: list) -> None:
    """Сортировка массива по возрастанию методом вставок. O(N**2).

    Идея:
        В начале каждой итерации цикла for есть отсортированный подмассив из элементов arr[:top], но в отсортированном порядке.

    Args:
        arr (list): исходный массив.

    Returns:
        None.
    """
    for top in range(1, len(arr)):
        k = top
        # and - ленивое(не будет вычислять 2 выражение, если первое ложно).
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1


def selection_sort(arr: list) -> None:
    """Сортировка массива по возрастанию методом выбора. O(N**2).

    Идея:
        В каждой итерации цикла for ищет минимальный элемент из подмассива arr[pos:] и меняет его местами с arr[pos].

    Args:
        arr (list): исходный массив.

    Returns:
        None.
    """
    n = len(arr)
    for pos in range(n - 1):
        # Находим индекс минимального элемента массива arr.
        k = min(range(pos, n), key=arr.__getitem__)
        arr[pos], arr[k] = arr[k], arr[pos]
    

def bubble_sort(arr: list) -> None:
    """Сортировка массива по возрастанию методом пузырька. O(N**2).

    Идея:
        В конце каждой итерации цикла (1) максимум из подмассива arr[:i + 1] стоит в arr[i].
        Цикл (2) обходит массив arr[:i], попутно меняя местами неотсортированные соседние элементы.
        Если к концу очередной итерации цикла (2) никаких обменов не произошло, то массив уже отсортирован.

    Args:
        arr (list): исходный массив.

    Returns:
        None.
    """
    for border in range(len(arr) - 1, 0, -1):  #(1).
        no_swap = True
        for j in range(border):  #(2).
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swap = False
        if no_swap:
            break


def merge_sort(arr: list) -> None:
    """Сортировка слиянием. O(N log N).

    Идея:
        Парадигма "разделяй и властвуй".
        Разделение:
            Делим массив arr на 2 подмассива длиной len(arr)//2. 
        Властвование:
            Рекурсивно сортируем эти 2 подмассива с использованием сортировки слиянием.
        Комбинирование:
            Соединяем два подмассива для получения окончательного отсортированного ответа.
        Рекурсия достигает своего нижнего предела, когда длина сортируемого массива меньше двух. В этом случае вся 
        работа уже сделана, поскольку такой массив уже является отсортированным.
    
    Args:
        arr (list): исходный массив.

    Returns:
        None.
    """
    def _merge(arr: list, p: int, q: int, r: int) -> None:
        """Сливает два подмассива arr[p:q+1] и arr[q+1:r+1] в один отсортированный, элементы которого заменяют текущие
        элементы подмассива arr[p:r+1]. O(N).

        Хитрость:
            В самый конец обоих подмассивов помещается бесконечно большое число. Благодаря этому в ходе каждой итерации
            цикла for не приходится проверять, вышел ли индекс за подмассив. А количество шагов нам заранее известно
            (r-p+1), так что после этого можно остановиться.

        Args:
            arr (list): массив.
            p (int): индекс начала левой границы.
            q (int): индекс конца левой и начала правой границ.
            r (int): индекс конца правой границы.
        
        Returns:
            None.
        """
        left = [arr[i + p] for i in range(q - p + 1)] + [float("inf")]
        right = [arr[j + q + 1] for j in range(r - q)] + [float("inf")]
        i = j = 0
        for k in range(p, r + 1):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
    
    def _merge_sort(arr: list, p: int, r: int) -> None:
        """Выполняет сортировку слиянием в подмассиве arr[p:r+1].

        Args:
            arr (list): массив.
            p (int): индекс начала границы.
            r (int): индекс конца границы.

        Returns:
            None.
        """
        if p < r:
            q = (p + r) // 2
            _merge_sort(arr, p, q)
            _merge_sort(arr, q + 1, r)
            _merge(arr, p, q, r)
    
    _merge_sort(arr, 0, len(arr) - 1)


def bin_search(seq, x):
    """Алгоритм бинарного поиска элемента x в последовательности seq. Последовательность должна быть 
    отсортирована по возрастанию! O(log N).

    Идея:
        Находим средний элемент последовательности (m). Если он меньше искомого, то сдвигаем  начало левой границы на 
        m + 1, иначе сдвигаем конец правой границы на m (учитываем, что seq[m] может быть равна x). Дожидаемся 
        схождения начала левой и конца правой границ и сравниваем элемент на месте схождения с искомым.

    Args:
        seq (list или tuple): упорядоченная по возрастанию последовательность.
        x (любой): искомый элемент.

    Returns:
        int или None: индекс элемента x, если этот элемент есть в последовательности seq, иначе None.
    """
    i, j = 0, len(seq) - 1
    while i < j:
        m = (i + j) // 2
        if x > seq[m]:
            i = m + 1
        else:
            j = m
    if seq[j] == x:
        return j
    return None


def inversions_num(arr: list) -> int:
    """Алгоритм для нахождения количества инверсий в массиве arr. O(N log N).
    
    Идея:
        Если i < j и arr[i] > arr[j], то пара (i, j) называется инверсией массива arr.
        Для достижения времени O(N log N) модифицируем сортировку слиянием. В функции 
        слияния (m_merge) есть такой шаг, когда текущий элемент левой части больше 
        текущего элемента правой части. Вот в этот момент нужно к (локальному) счётчику
        инверсий (invcount) добавить количество ещё неиспользованных элементов левой 
        половины (не учитывая сигнальный элемент). А в рекурсивной функции m_merge_sort 
        нужно сложить количество инверсий в левой половине, количество в правой, и 
        количество инверсий, возникающих при слиянии этих половин.
    
    Args:
        arr (list): исходный массив.

    Returns:
        int: 
    """
    def m_merge(arr: list, p: int, q: int, r: int) -> int:
        left = [arr[i + p] for i in range(q - p + 1)] + [float("inf")]
        right = [arr[j + q + 1] for j in range(r - q)] + [float("inf")]
        n = len(left) - 1
        i = j = invcount = 0
        for k in range(p, r + 1):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                invcount += n - i
                arr[k] = right[j]
                j += 1
        return invcount
    
    def m_merge_sort(arr: list, p: int, r: int) -> int:
        if p < r:
            q = (p + r) // 2
            return m_merge_sort(arr, p, q) + m_merge_sort(arr, q + 1, r) + m_merge(arr, p, q, r)
        return 0
    
    arr_copy = arr.copy()
    return m_merge_sort(arr_copy, 0, len(arr) - 1)


def gcd(a: int, b: int) -> int:
    """Алгоритм нахождения наибольшего общего делителя чисел a и b.

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: НОД чисел a и b.
    """
    return a if b == 0 else gcd(b, a % b)
