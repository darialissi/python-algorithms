"""
Создайте стек на базе статического массива. 
Класс для управления стеком должен называться Stack 
    и содержать два метода: .push() для добавления новых значений и .pop() для извлечения верхнего элемента.

В случае если в стеке не осталось элементов, то .pop() должен вернуть None.
Если стек полностью заполнен, то очередной вызов .push() должен возбудить исключение OverflowError.
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
    Стек на базе статического массива.
    """

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.length:
            value = self.data[self.length - 1]
            self.length -= 1
            return value

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        if self.length == self.size:
            raise OverflowError
         
        self.data[self.length] = value
        self.length += 1


stack = Stack(3)

stack.push(12)
stack.push(7)
stack.push(6)

print(stack.pop())

print(stack.pop())

print(stack.pop())

print(stack.pop())