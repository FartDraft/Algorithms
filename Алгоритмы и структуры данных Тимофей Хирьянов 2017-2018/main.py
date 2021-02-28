from math import trunc, sqrt
from random import choice


def sieve(n: int) -> list:
    """Обычное решето Эратосфена. Алгоритм проверки чисел на простоту до заданного 
        натурального числа (включительно) путём постепенного отсеивания составных чисел.

    Args:
        n (int):  натуральное число, включительно до которого будут проверены на простоту.

    Returns:
        list: массив bool значений. 
            Каждый индекс соответствует числу. True - если число простое, иначе - False.
    """
    assert n > 2, "n меньше чем 2"
    ret = [False, False] + [True] * (n - 1)
    for k in range(2, trunc(sqrt(n)) + 1):
        if ret[k]:
            for i in range(k * k, n + 1, k):
                ret[i] = False
    return ret


def insertion_sort(arr: list) -> list:
    """Сортировка массива по возрастанию методом вставок. O(N**2).

    Идея:
        В начале каждой итерации цикла for есть отсортированный подмассив из элементов arr[:top], но в отсортированном порядке.

    Args:
        arr (list): исходный массив.

    Returns:
        list: отсортированный по возрастанию массив arr.
    """
    for top in range(1, len(arr)):
        k = top
        # and - ленивое(не будет вычислять 2 выражение, если первое ложно).
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1


def selection_sort(arr: list) -> list:
    """Сортировка массива по возрастанию методом выбора. O(N**2).

    Идея:
        В каждой итерации цикла for ищет минимальный элемент из подмассива arr[pos:] и меняет его местами с arr[pos].

    Args:
        arr (list): исходный массив.

    Returns:
        list: отсортированный по возрастанию массив arr.
    """
    n = len(arr)
    for pos in range(n - 1):
        # Находим индекс минимального элемента массива arr.
        k = min(range(pos, n), key=arr.__getitem__)
        arr[pos], arr[k] = arr[k], arr[pos]
    

def bubble_sort(arr: list) -> list:
    """Сортировка массива по возрастанию методом пузырька. O(N**2).

    Идея:
        В конце каждой итерации цикла (1) максимум из подмассива arr[:i + 1] стоит в arr[i].
        Цикл (2) обходит массив arr[:i], попутно меняя местами неотсортированные соседние элементы.
        Если к концу очередной итерации цикла (2) никаких обменов не произошло, то массив уже отсортирован.

    Args:
        arr (list): исходный массив.

    Returns:
        list: отсортированный по возрастанию массив arr.
    """
    for border in range(len(arr) - 1, 0, -1):  #(1).
        no_swap = True
        for j in range(border):  #(2).
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swap = False
        if no_swap:
            break


def gcd(a: int, b: int) -> int:
    """Алгоритм нахождения наибольшего общего делителя чисел a и b.

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: НОД чисел a и b.
    """
    return a if b == 0 else gcd(b, a % b)


def fast_pow(a: float, n: int) -> int:
    """Алгоритм быстрого возведения числа a в степень n.

    Args:
        a (float): число.
        n (int): степень.

    Returns:
        int: результат.
    """
    if n == 0:
        return 1
    elif n % 2:
        return fast_pow(a, n - 1) * a
    else:
        return fast_pow(a * a, n // 2)


def hanoi_towers(n: int, start: int, finish: int) -> None:
    """Алгоритм для решения головоломки "Ханойские башни". Суть головоломки:
    Есть три стержня, пронумерованных числами 1, 2, 3. На стержень start надета пирамидка из n дисков различного диаметра в порядке 
    возрастания диаметра. Диски можно перекладывать с одного стержня на другой по одному, при этом диск нельзя класть на диск меньшего 
    диаметра. Необходимо переложить всю пирамидку со стержня start на стержень finish за минимальное число перекладываний.

    Args:
        n (int): количество дисков.
        start (int): порядковый номер стартового стержня.
        finish (int): порядковый номер конечного стержня.
    """
    if n > 0:
        tmp = 6 - start - finish
        hanoi_towers(n - 1, start, tmp)
        print(f"Перенесите диск {n} со стержня {start} на стержень {finish}.")
        hanoi_towers(n - 1, tmp, finish)


def quick_sort(arr: list) -> list:
    """Сортировка Тони Хоара. O(NlogN).
    Идея:
        Парадигма "разделяй и властвуй".
        Разделение:
            Выбираем из массива элемент, называемый опорным. Разбиваем массив на три подмассива: "элементы меньшие 
            опорного", "равные" и "большие".
        Властвование:
            Рекурсивно сортируем подмассивы "меньших" и "больших" с использованием сортировки Тони Хоара.
        Комбинирование:
            Копируем "меньшие", "равные" и "большие" подмассивы в массив arr на нужное место.
        Рекурсия достигает своего нижнего предела, когда длина сортируемого массива меньше двух. В этом случае вся 
        работа уже сделана, поскольку такой массив уже является отсортированным

    Args:
        arr (list): исходный массив.

    Returns:
        list: отсортированный по возрастанию массив arr.
    """
    if len(arr) < 2:
        return
    pivot = choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [pivot] * arr.count(pivot)
    greater = [x for x in arr if x > pivot]
    quick_sort(less)
    quick_sort(greater)
    for i, x in enumerate(less + equal + greater):
        arr[i] = x


def merge_sort(arr: list) -> list:
    """Сортировка слиянием. O(N log N).
    Идея:
        Парадигма "разделяй и властвуй".
        Разделение:
            Делим массив arr на 2 подмассива длиной len(arr)//2. 
        Властвование:
            Рекурсивно сортируем эти 2 подмассива с использованием сортировки слияением.
        Комбинирование:
            Соединяем два подмассива для получения окончательного отсортированного ответа.
        Рекурсия достигает своего нижнего предела, когда длина сортируемого массива меньше двух. В этом случае вся 
        работа уже сделана, поскольку такой массив уже является отсортированным.

    Args:
        arr (list): исходный массив.

    Returns:
        list: отсортированный по возрастанию массив arr.
    """
    def _merge(arr: list, p: int, q: int, r: int) -> None:
        """Сливает два подмассива arr[p:q+1] и arr[q+1:r] в один отсортированный, элементы которого заменяют текущие
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
        """
        if p < r:
            q = (p + r) // 2
            _merge_sort(arr, p, q)
            _merge_sort(arr, q + 1, r)
            _merge(arr, p, q, r)
    
    _merge_sort(arr, 0, len(arr) - 1)


def bin_search(arr, x):
    """Алгоритм бинарного поиска элемента x в массиве arr. Массив должен быть отсортирован! O(logN).

    Идея:
        Находим средний элемент последовательности (m). Если он меньше искомого, то сдвигаем  начало левой границы на 
        m + 1, иначе сдвигаем конец правой границы на m (учитываем, что arr[m] может быть равна x). Дожидаемся 
        схождения начала левой и конца правой границ и сравниваем элемент на месте схождения с искомым.

    Args:
        arr (list or tuple): упорядоченная последовательность.
        x (any): искомый элемент.

    Returns:
        int or None: индекс если элемент x есть в массиве arr, иначе None.
    """
    i, j = 0, len(arr) - 1
    while i < j:
        m = (i + j) // 2
        if x > arr[m]:
            i = m + 1
        else:
            j = m
    if arr[j] == x:
        return j
    else:
        return None
