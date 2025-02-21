"""
Создайте очередь на базе двунаправленного связного списка. 
Класс для управления очередью должен называться Queue и содержать два метода: 
    .enqueue() для добавления новых значений и .dequeue() для извлечения элемента. .dequeue() должен возвращать значение элемента.

В случае если в очереди не осталось элементов, то .dequeue() должен вернуть None.
Считаем, что очередь на базе связного списка не ограничена по количеству элементов.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node()

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        node = Node(value)
        
        if self.top.next_node:
            self.top.next_node.prev_node = node
            
        node.next_node = self.top.next_node
        node.prev_node = self.top
        self.top.next_node = node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if not self.top.next_node:
            return
        
        current = self.top
        
        while current.next_node:
            current = current.next_node
            
        value = current.value
        current.prev_node.next_node = None
        
        return value
    

queue = Queue()

queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())