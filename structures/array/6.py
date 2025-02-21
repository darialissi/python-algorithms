"""
Запрограммируйте метод .remove() для удаления элементов из статического массива по значению.
Метод должен принимать один аргумент: значение для удаления.

Если в массиве несколько одинаковых элементов подходящих для удаления, то удалять нужно все.

Попробуйте написать алгоритм, который будет работать за время O(N), то есть все манипуляции должны произойти за один проход.
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
        """
        Удаляет все элементы со значением value.
        Время работы O(N).
        """
        shift = 0

        for i in range(self.length):
            if self.data[i] == value:
                # Увеличиваем сдвиг
                shift += 1
            else:
                # Сдвигаем элемент влево на shift позиций
                self.data[i - shift] = self.data[i]

        self.length -= shift

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
    

array = Array(5)

array.append(6)
array.append(2)
array.append(1)
array.append(2)
array.append(9)

print(array)

array.remove(2)
print(array)