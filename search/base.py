"""
Бинарный поиск. O(logN).
Отсортированный массив.
"""

def binary_search(array, value):
    """
    Возвращает индекс искомого элемента (value) в отсортированном массиве.
    Если в массиве более одного искомого элемента,
    то функция не гарантирует, что найденный будет первым.
    Возвращает -1 если элемент не найден.
    """
    min_index = 0
    max_index = len(array) - 1

    # Цикл до тех пор, пока min и max не встретятся
    while min_index <= max_index:

        # Вычисляем средний элемент.
        middle_index = (min_index + max_index) // 2

        # Меняем max_index и min_index.
        if value < array[middle_index]:
            max_index = middle_index - 1
        elif value > array[middle_index]:
            min_index = middle_index + 1
        else:
            return middle_index

    return -1

def binary_search_rec(array, value, min_index=None, max_index=None):
    """
    Рекурсивный алгоритм.
    """
    
    # Если это первый запуск, то вычисляем значения min_index и max_index.
    if min_index is None:
        min_index = 0
    if max_index is None:
        max_index = len(array) - 1

    # Вычисляем средний индекс.
    middle_index = (min_index + max_index) // 2

    # Сравниваем искомый элемент с текущим.
    if value == array[middle_index]:
        return middle_index

    # Проверка выхода индексов за пределы.
    if min_index > max_index:
        return -1

    # Обновляем минимум и максимум.
    if value > array[middle_index]:
        min_index = middle_index + 1
    else:
        max_index = middle_index - 1

    # Рекурсивный вызов
    return binary_search(array, value, min_index, max_index)

"""
Интерполяционный поиск. O(log(logN)).
Отсортированный массив с равномерным распределением.
"""

def interpolation_search(array, value):
    """
    Возвращает индекс значения value в массиве array.
    Если в массиве более одного искомого элемента,
    то функция не гарантирует, что найденный будет первым.
    Возвращает -1 если элемент не найден.
    """
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        
        # Проверка равенства индексов
        if min_index == max_index:
            if array[min_index] == value:
                return min_index
            return -1

        # Поиск среднего элемента.
        middle_index = min_index + (max_index - min_index) * \
              (value - array[min_index]) // (array[max_index] - array[min_index])

        if (middle_index < min_index) or (middle_index > max_index):
            return -1

        # Продолжаем поиск или возвращаем найденный индекс.
        if array[middle_index] < value:
            min_index = middle_index + 1
        elif array[middle_index] > value:
            max_index = middle_index - 1
        else:
            return middle_index

    return -1