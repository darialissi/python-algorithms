"""
Создайте стек на базе связного списка. 
Класс для управления стеком должен называться Stack 
    и содержать два метода: .push() для добавления новых значений и .pop() для извлечения верхнего элемента.

При извлечении элемента, .pop() должен возвращать его значение (value).
В случае если в стеке не осталось элементов, то .pop() должен вернуть None.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.top = Node()

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        node = self.top.next_node
        
        if not node:
            return
        
        self.top.next_node = node.next_node
        return node.value

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        node = Node(value)
        
        node.next_node = self.top.next_node
        self.top.next_node = node


stack = Stack()

stack.push(12)
stack.push(7)
stack.push(6)

print(stack.pop())

print(stack.pop())

print(stack.pop())

print(stack.pop())