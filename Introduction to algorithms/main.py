def inversions_num(arr: list) -> int:  #*
    """Алгоритм для нахождения количества инверсий в массиве arr. O(N log N).
    Если i < j и arr[i] > arr[j], то пара (i, j) называется инверсией массива arr.
    Для достижения O(N log N) модифицируем сортировку слиянием. В функции 
    слияния (m_merge) есть такой шаг, когда текущий элемент левой части меньше 
    текущего элемента правой части. Вот в этот момент нужно к (локальному) счётчику
    инверсий (invcount) добавить количество ещё неиспользованных элементов левой 
    половины (не учитывая сигнальный элемент). А в рекурсивной функции m_merge_sort 
    нужно сложить количество инверсий в левой половине, количество в правой, и 
    количество инверсий, возникающих при слиянии этих половин.
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
