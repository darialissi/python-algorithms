"""
Создадим эмуляцию статического массива на базе списков Array.

Реализуйте метод .append() для вставки элементов в конец массива.
Метод должен принимать один аргумент — значение для вставки.

В случае если массив полностью заполнен, 
    при добавлении нового значения должно срабатывать исключение OverflowError.
"""

class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        # Проверяем заполненность массива
        if self.length == self.size:
            raise OverflowError

        # Добавляем новый элемент
        self.data[self.length] = value

        # Увеличиваем длину
        self.length += 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
    

array = Array(3)
print(array.size)

print(array.length)

print(array)

array.append(20)
array.append(10)
array.append(30)
print(array)

array.append(40)