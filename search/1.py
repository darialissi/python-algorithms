"""
Если в массиве несколько одинаковых элементов, 
    то оригинальный алгоритм бинарного поиска не гарантирует, 
        что будет возвращен индекс первого вхождения элемента. 

Однако, можно модифицировать алгоритм так, чтобы он возвращал первое вхождение элемента.

Передаваемые числа массива предварительно отсортированы.
Программа должна вывести в консоль индекс первого вхождения элемента. 
Если элемента в массиве нет, то она должна вывести -1.
"""

def binary_search(array, value):
    """
    Первое вхождение

    -1 - элемент не найден
    """

    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:

        middle_index = (min_index + max_index) // 2

        if array[middle_index] == value and (middle_index == 0 or value > array[middle_index - 1]):
            return middle_index
        elif value > array[middle_index]:
            min_index = middle_index + 1
        else:
            max_index = middle_index - 1

    return -1


values = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 5, 6, 7]

print(binary_search(values, 2))
print(binary_search(values, 1))