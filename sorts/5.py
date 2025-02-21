"""
Функция bucketsort() из урока «Блочная сортировка» сортирует элементы массива в прямом порядке.
Модифицируйте функцию так, чтобы она сортировала данные в обратном порядке.
"""

class Cell:
    """
    Ячейка для сортированного связного списка.
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


def bucketsort(array, num_buckets):
    """
    Блочная сортировка массива array.
    """

    # Создаем блоки, в которые помещаем пустые связные списки.
    buckets = []
    for i in range(num_buckets):
        buckets.append(Cell())

    # Вычисляем максимальны элемент в массиве.
    max_value = max(array)

    # Рассчитываем количество значений в корзине.
    items_per_bucket = (max_value + 1) / num_buckets

    # Распределяем данные по корзинам.
    for value in array:
        # Вычисляем номер корзины.
        backet_num = int(value / items_per_bucket)

        # Вставляем элемент в корзину сразу со сортировкой.
        after_me = buckets[backet_num]
        while (after_me.next_node is not None) and (after_me.next_node.value > value):
            after_me = after_me.next_node
        cell = Cell(value, after_me.next_node)
        after_me.next_node = cell

    # Отправляем элементы обратно в массив.
    index = 0
    for i in range(num_buckets-1, -1, -1):
        # Копируем значения из корзины в массив.
        cell = buckets[i].next_node
        while cell is not None:
            array[index] = cell.value
            index += 1
            cell = cell.next_node


array = [1, 2, 3, 5, 7, 2, 4, 2, 4, 5, 6]

bucketsort(array, 5)
print(array)