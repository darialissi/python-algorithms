"""
Добавьте в массив Array метод: .reverse(), который развернет массив в обратном порядке.

Сложность такого алгоритма будет O(N), 
    однако на практике нужно пройти только половину массива, меняя на каждом шаге два элемента (слева и справа).
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

    def reverse(self):
        """
        Разворачивает массив.
        """
        for i in range(self.length // 2):
            self.data[i], self.data[self.length - i - 1] = self.data[self.length - i - 1], self.data[i]

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

array.reverse()

print(array)