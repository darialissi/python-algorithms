"""
Добавьте в массив Array три дополнительных метода: .min(), .max() и .avg(). 
В качестве среднего рассчитывайте среднее арифметическое.
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

        self._mx = float('-inf')
        self._mn = float('inf')
        self._sm = 0

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        
        if value > self._mx:
            self._mx = value

        if value < self._mn:
            self._mn = value

        self._sm += value
        self.data[self.length] = value
        self.length += 1

    def min(self):
        """
        Минимальное значение в массиве.
        """
        return self._mn


    def max(self):
        """
        Максимальное значение в массиве.
        """
        return self._mx

    def avg(self):
        """
        Среднее значение в массиве.
        """
        return self._sm / self.length

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

print(array.min())

print(array.max())

print(array.avg())