"""
Модифицируйте функцию bubblesort() так, чтобы она  упорядочивала массив в обратном порядке.
"""

def bubblesort(array):
    n = 1
    
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        n += 1


lst = [6, 4, 2, 9, 1, 3]
bubblesort(lst)

print(lst)