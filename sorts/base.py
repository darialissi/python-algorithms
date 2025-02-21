"""
Пузырьковая сортировка. O(N^2).
"""

def bubblesort(values):
    # Количество пузырьков, которые опустились на дно (для оптимизации).
    n = 1

    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(len(values) - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False

        n += 1

"""
Сортировка выбором. O(N^2).

В каждой итерации находим min/max в текущей части и ставим его крайним в сформированную часть.
"""

def selectionsort(values):
    for i in range(len(values) - 1):
        min_idx = i

        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j

        if i != min_idx:
            values[i], values[min_idx] = values[min_idx], values[i]

"""
Сортировка вставками. O(N^2).

Для каждого следующего элемента находим подходящее место в отсортированной части.

Эффективна при частично отсортированном массиве.
"""

def insertionsort(array):
    i = 1

    while i < len(array):
        j = i - 1
        # Проходим по отсортированной части в обратную строну.
        # До тех пор пока значение текущего элемента array[j+1]
        # меньше значения предыдущего array[j].
        while j >= 0 and array[j+1] < array[j]:
            array[j+1], array[j] = array[j], array[j+1]
            j -= 1
        i += 1

"""
Быстрая сортировка. O(N*logN) или O(N^2).
"""

def quicksort(array):
    if len(array) <= 1:
       return array
    
    divider = array[0]

    equal = [divider]
    greater = []
    less = []

    for i in array:
        if i < divider:
            less.append(i)
        elif i > divider:
            greater.append(i)
        else:
            equal.append(i)

    return quicksort(less) + equal + quicksort(greater)

"""
Сортировка слиянием. O(N*logN).
"""

def mergesort(array): 
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    mergesort(left)
    mergesort(right)

    # Индексы left, right, array
    i = j = k = 0

    # Сравниваем левый и правый элемент и вставляем в итоговый массив
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            array[k] = left[i] 
            i += 1
        else: 
            array[k] = right[j] 
            j += 1

        k += 1

    # Оставшиеся части left / right
    if i < len(left):
        array[k:] = left[i:]
    if j < len(right):
        array[k:] = right[j:]

"""
Сортировка подсчетом. O(N + M).

Подходит для сортировки большого массива целых чисел с небольшим диапазоном.
"""

def countingsort(values, max_value):
    
    # Создаем массив-счетчик.
    counts = [0] * (max_value + 1)

    # Считаем количество значений основного массива.
    for value in values:
        counts[value] += 1

    index = 0

    # Копируем значения обратно в массив.
    for i in range(max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1



