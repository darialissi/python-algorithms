"""
В классе Array (статический массив) есть метод .remove(), который удаляет из массива элементы по их индексу. 
Фактически, при работе этого метода вместо реального удаления происходит установка None на место значения. 
При этом сдвига элементов влево не происходит, что позволяет удалять элементы за время O(1). 
Однако из-за такого поведения массив может стать разряженным (с пустыми элементами в середине).

Чтобы избавиться от разряженности, в массиве предусмотрен метод .compress(), вам предстоит его запрограммировать. 
А именно, нужно сделать так, чтобы все элементы со значениями оказались слева, а None (если они есть) ушли вправо.

Например, из такого массива [2, None, 1, 3, None, None, 5, 4] вы должны получить [2, 1, 3, 5, 4, None, None, None].

Попробуйте решить задание за один проход по массиву.
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

        # Позиция для вставки
        self.append_index = 0

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.append_index] = value
        self.append_index += 1
        self.length += 1

    def remove(self, index):
        """
        Удаляет элемент (устанавливает None) по его индексу.
        Время работы O(1).
        """

        # Удаление имеет смысл только если элемент есть
        if self.data[index] is not None:

            # Удаляем и уменьшаем длину
            self.data[index] = None
            self.length -= 1

            # Если мы удаляем элемент, перед которым можно вставить новый элемент,
            # то сдвигаем append_index.
            if index == self.append_index - 1:
                self.append_index = index

    def compress(self):
        """
        Сжимаем массив
        """
        idx_none = 0

        for i in range(self.size):
            if self.data[i] is not None:
                if i != idx_none:
                    self.data[idx_none], self.data[i] = self.data[i], self.data[idx_none]
                idx_none += 1

        self.append_index = idx_none

    def __str__(self):
        """
        Возвращает весь массив в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"
    

array = Array(8)

array.append(2)
array.append(6)
array.append(1)
array.append(3)
array.append(7)
array.append(9)
array.append(5)
array.append(4)

print(array)

array.remove(2)
array.remove(4)
array.remove(5)

print(array)

array.compress()

print(array)