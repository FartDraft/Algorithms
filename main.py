__author__ = "Afanasin Egor"
# При нахождении ошибки в работе функции или неточности в документации обращаться по почте:
__email__ = "fartdraft@gmail.com"


def is_simple(num: int) -> bool:
    """Проверка числа num на простоту.

    Args:
        num (int): натуральное число.

    Returns:
        bool: True - если число num простое, иначе False.
    """
    from math import trunc, sqrt

    if num == 2 or num == 3:
        return True
    elif num < 2 or not num % 2 or not num % 3:
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
    from math import trunc, sqrt

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
    """Сортировка массива по возрастанию методом вставок. Θ(N**2).

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
    """Сортировка массива по возрастанию методом выбора. Θ(N**2).

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
    """Сортировка массива по возрастанию методом пузырька. Θ(N**2).

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
    """Сортировка слиянием. Θ(N log N).

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
        элементы подмассива arr[p:r+1]. Θ(N).

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
            # Разделение.
            q = (p + r) // 2
            # Властвование.
            _merge_sort(arr, p, q)
            _merge_sort(arr, q + 1, r)
            # Комбинирование.
            _merge(arr, p, q, r)
    
    _merge_sort(arr, 0, len(arr) - 1)


def bin_search(seq, x):
    """Алгоритм бинарного поиска элемента x в последовательности seq. Последовательность должна быть 
    отсортирована по возрастанию! Θ(log N).

    Идея:
        Находим средний элемент последовательности (seq[m]). Если он меньше искомого, то сдвигаем начало левой границы на 
        место m + 1, иначе сдвигаем конец правой границы на m (учитываем, что seq[m] может быть равна x). Дожидаемся 
        схождения левой и правой границ и сравниваем элемент на месте остановки правой границы (именно она отвечает за 
        местонахождение элемента x) с искомым.

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
    """Алгоритм для нахождения количества инверсий в массиве arr. Θ(N log N).
    
    Идея:
        Если i < j и arr[i] > arr[j], то пара (i, j) называется инверсией массива arr.
        Для достижения времени Θ(N log N) модифицируем сортировку слиянием. В функции 
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


def find_maximum_subarray(arr: list) -> tuple:
    """Алгоритм для нахождения непустого непрерывного подмассива массива arr, значения которого имеют наибольшую сумму. 
    Такой подмассив я называю максимальным. Возвращает (-1, -1, 0), если в исходном массиве arr нет ни одного 
    положительного числа. Θ(N).

     Идея:
        Максимальный подмассив массива arr[:i+1] представляет собой либо максимальный подмассив массива arr[:i], либо
        подмассив arr[low:i+1], для некоторого 0 <= low <= i. Текущий подмассив arr[low:i+1] рассматривается, пока его 
        сумма (sm) больше 0, если же значение arr[i] привело sm в отрицательное значение, то рассматривается подмассив,
        начинающийся со следующего элемента (low = i + 1; sm = 0), так как если значение этого элемента будет положительным,
        то он гарантировано создаст единичный подмассив (из него самого) с локальной суммой большей, чем эта. Если же
        элемент x положителен и текущая сумму больше максимальной, то текущий подмассив arr[low:i+1] становится максимальным.

    Args:
        arr (list): исходный массив.

    Returns:
        tuple: кортеж длиной 3:
            1 элемент (int): индекс начала максимального подмассива.
            2 элемент (int): индекс конца максимального подмассива.
            3 элемент (int): сумма значений элементов максимального подмассива.
    """
    max_low = max_high = -1
    max_sum = low = sm = 0
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


def Vinograd_Strassen(a: list, b: list) -> list:
    """Алгоритм Винограда-Штрассена для умножения квадратных матриц. Θ(N**log2(7)), O(N**2,81).
    Матрицы a и b могут быть перемножены, если они совместимы в том смысле, что число столбцов матрицы a равно числу
    строк матрицы b. Данная реализация алгоритма НЕ РАБОТАЕТ для прямоугольных матриц a и b вида m*n и n*p соответственно.
    Это было сделано в целях ускорения времени выполнения.

    Идея:
        A11 A12     B11 B12     C11 C12
        A21 A22  *  B21 B22  =  C21 C22
        
        S1 = A21 + A22
        S2 = S1 - A11
        S3 = A11 - A21
        S4 = A12 - S2
        S5 = B12 - B11
        S6 = B22 - S5
        S7 = B22 - B12
        S8 = S6 - B21
        
        P1 = S2 * S6
        P2 = A11 * B11
        P3 = A12 * B21
        P4 = S3 * S7
        P5 = S1 * S5
        P6 = S4 * B22
        P7 = A22 * S8
        
        T1 = P1 + P2
        T2 = T1 + P4
        
        C11 = P2 + P3
        C12 = T1 + P5 + P6
        C21 = T2 - P7
        C22 = T2 + P5

    Args:
        a (list): матрица размером N*N.
        b (list): матрица размером N*N.

    Returns:
        list: матрица размером N*N произведения матриц a и b.
    """

    def _Vinograd_Strassen(a: list, b: list):
        n = len(a)
        # Базовый случай.
        if n == 1:
            return [[a[0][0] * b[0][0]]]
        
        # Рекурсивный случай.
        n2 = n // 2

        A11 = [[a[i][j] for j in range(n2)] for i in range(n2)]
        A12 = [[a[i][j] for j in range(n2, n)] for i in range(n2)]
        A21 = [[a[i][j] for j in range(n2)] for i in range(n2, n)]
        A22 = [[a[i][j] for j in range(n2, n)] for i in range(n2, n)]
        B11 = [[b[i][j] for j in range(n2)] for i in range(n2)]
        B12 = [[b[i][j] for j in range(n2, n)] for i in range(n2)]
        B21 = [[b[i][j] for j in range(n2)] for i in range(n2, n)]
        B22 = [[b[i][j] for j in range(n2, n)] for i in range(n2, n)]

        S1 = [[A21[i][j] + A22[i][j] for j in range(n2)] for i in range(n2)]
        S2 = [[S1[i][j] - A11[i][j] for j in range(n2)] for i in range(n2)]
        S3 = [[A11[i][j] - A21[i][j] for j in range(n2)] for i in range(n2)]
        S4 = [[A12[i][j] - S2[i][j] for j in range(n2)] for i in range(n2)]
        S5 = [[B12[i][j] - B11[i][j] for j in range(n2)] for i in range(n2)]
        S6 = [[B22[i][j] - S5[i][j] for j in range(n2)] for i in range(n2)]
        S7 = [[B22[i][j] - B12[i][j] for j in range(n2)] for i in range(n2)]
        S8 = [[S6[i][j] - B21[i][j] for j in range(n2)] for i in range(n2)]

        P1 = _Vinograd_Strassen(S2, S6)
        P2 = _Vinograd_Strassen(A11, B11)
        P3 = _Vinograd_Strassen(A12, B21)
        P4 = _Vinograd_Strassen(S3, S7)
        P5 = _Vinograd_Strassen(S1, S5)
        P6 = _Vinograd_Strassen(S4, B22)
        P7 = _Vinograd_Strassen(A22, S8)

        T1 = [[P1[i][j] + P2[i][j] for j in range(n2)] for i in range(n2)]
        T2 = [[T1[i][j] + P4[i][j] for j in range(n2)] for i in range(n2)]

        C = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n2):
            for j in range(n2):
                C[i][j] = P2[i][j] + P3[i][j]
        for i in range(n2):
            for j in range(n2):
                C[i][n2 + j] = T1[i][j] + P5[i][j] + P6[i][j]
        for i in range(n2):
            for j in range(n2):
                C[n2 + i][j] = T2[i][j] - P7[i][j]
        for i in range(n2):
            for j in range(n2):
                C[n2 + i][n2 + j] = T2[i][j] + P5[i][j]

        return C

    from math import trunc, log2

    assert len(a) == len(a[0]) == len(b) == len(b[0]) , "Матрицы a и b должны быть квадратными."

    # Является ли сторона квадратной матриц степенью двойки.
    n = len(a) 
    n1 = log2(n)

    # Если да - запускаем алгоритм без предварительных изменений матриц a и b.
    if n1 % 1 == 0.0:
        C = _Vinograd_Strassen(a, b)
        return C

    # Если нет - дополняем входные матрицы a и b до следующей по величине степени двойки.
    n1 = pow(2, trunc(n1) + 1)   
    a = [a[i] + [0] * (n1 - n) for i in range(n)] + [[0] * n1 for _ in range(n1 - n)]
    b = [b[i] + [0] * (n1 - n) for i in range(n)] + [[0] * n1 for _ in range(n1 - n)]
    C = _Vinograd_Strassen(a, b)
    # Обрезаем добавленные нули из возвращаемой матрицы, приводя её к исходным размерам.
    return [[C[i][j] for j in range(n)] for i in range(n)]


def gcd(a: int, b: int) -> int:
    """Алгоритм нахождения наибольшего общего делителя чисел a и b.

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: НОД чисел a и b.
    """
    return a if b == 0 else gcd(b, a % b)
