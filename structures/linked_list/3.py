"""
Добавьте метод .length(), который будет возвращать длину связного списка.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)

# Вариант с проходом в методе
class List:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

    def length(self):
        length = 0
        
        current = self.head
        
        while current is not None:
            length += 1
            current = current.next_node
            
        return length

# Вариант с хранением длины в атрибуте
class List2:

    def __init__(self):
        self.head = None
        self._length = 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self._length += 1
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)
        
        self._length += 1

    def length(self):
        return self._length
    

lst = List()
lst.append("A")
lst.append("B")
lst.append("C")
print(lst.length())

lst = List2()
lst.append("A")
lst.append("B")
lst.append("C")
print(lst.length())