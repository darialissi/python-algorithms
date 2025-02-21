"""
Расширьте класс Stack дополнительными методами:

.peek() — должен возвращать значение верхнего элемента в стеке без его удаления.
    Если стек пустой, то .peek() должен вернуть None.
.count() — должен возвращать количество элементов в стеке.
.clear() — должен очищать стек.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:
    """
    Стек на базе связного списка.
    """
    def __init__(self):
        self.top = Node()

        # Определяем начальное значение для количества элементов.
        self._count = 0

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Получаем верхний элемент
        top = self.top.next_node

        # Перестраиваем связи и возвращаем значение
        if top:
            self.top.next_node = top.next_node
            self._count -= 1
            return top.value

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        # Добавляем элемент в начало связного списка
        new_node = Node(value)

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

        self._count += 1

    def clear(self):
        """
        Очищает стек.
        """
        self.top.next_node = None
        self._count = 0

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        if self.top.next_node:
            return self.top.next_node.value

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        return self._count
    

stack = Stack()

stack.push(12)
stack.push(7)
stack.push(6)

print(stack.peek())

print(stack.count())

stack.clear()
print(stack.count())

print(stack.peek())