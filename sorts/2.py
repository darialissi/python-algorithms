"""
Модифицируйте стандартный алгоритм сортировки подсчетом так, 
    чтобы он мог работать как с положительными, так и с отрицательными числами.
"""

def countingsort(values):

    # Вычисляем min_value/max_value.
    max_value = values[0]
    min_value = values[0]

    for value in values[1:]:
        max_value = max(value, max_value)
        min_value = min(value, min_value)

    # Создаем массив-счетчик.
    counts = [0] * (max_value - min_value + 1)

    # Считаем количество значений основного массива.
    for value in values:
        counts[value - min_value] += 1

    # Копируем значения обратно в массив.
    index = 0
    for i in range(max_value - min_value + 1):
        for j in range(counts[i]):
            values[index] = i + min_value
            index += 1


lst = [7, 8, 7, 3, 6, 5, 1, 3, 3, 1]
countingsort(lst)

print(lst)