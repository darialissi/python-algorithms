"""
Иногда в алгоритмах используются два стека с ограниченным общим размером. 
В этом случае данные сохраняются в одном массиве с разных сторон
    (массив заполняется слева направо для левой стороны и справа налево для правой стороны)

Создайте двойной стек на базе статического массива. 

Класс для управления стеком должен называться Stack и содержать пять методов:
    .push_left() для добавления новых значений слева.
    .push_right() для добавления новых значений справа.
    .pop_left() для извлечения верхнего элемента слева.
    .pop_right() для извлечения верхнего элемента права.
    .clear() для очистки стека.

В случае если в стеке не осталось элементов, то .pop_left() и .pop_right() должны возвращать None.
Если стек полностью заполнен, то очередной вызов .push_left() или .push_right() должен возбудить исключение OverflowError.
"""

class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        
        self.left_top = 0
        self.right_top = -1

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.left_top == 0:
            return
            
        self.left_top -= 1
        self.length -= 1
        value = self.data[self.left_top]
        return value

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        if self.right_top == -1:
            return
        
        self.right_top += 1
        self.length -= 1
        value = self.data[self.right_top]
        return value

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        if self.length == self.size:
            raise OverflowError
            
        self.data[self.left_top] = value
        self.left_top += 1
        self.length += 1

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        if self.length == self.size:
            raise OverflowError
            
        self.data[self.right_top] = value
        self.right_top -= 1
        self.length += 1

    def clear(self):
        """
        Очищает стек.
        """
        self.left_top = 0
        self.right_top = -1
        self.length = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"
    

stack = Stack(4)

stack.push_left(12)
stack.push_left(7)
stack.push_left(6)
stack.push_right(8)

print(stack.pop_left())

print(stack.pop_right())

print(stack.pop_right())

stack.push_left(3)
stack.push_left(5)
stack.push_left(9)