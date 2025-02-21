"""
Запрограммируйте метод .remove() для удаления элемента из статического массива по значению.
Метод должен принимать один аргумент: значение для удаления.

Если в массиве несколько одинаковых элементов подходящих для удаления, то удалять нужно только первый.
"""

class Array:
    """
    Линейный статический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def remove(self, value):
        index = None

        # Находим индекс элемента
        for i in range(self.length):
            if self.data[i] == value:
                index = i
                break

        if index is None:
            return
        
        self.length -= 1

        # Смещаем элементы массива
        for i in range(index, self.length):
            self.data[i] = self.data[i + 1]

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
    
array = Array(4)

array.append(6)
array.append(2)
array.append(1)
array.append(9)

print(array)

array.remove(6)
print(array)

array.remove(1)
print(array)
