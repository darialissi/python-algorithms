"""
Расширьте класс Queue дополнительными методами:

.peek() — должен возвращать значение первого элемента в очереди без его удаления.
    Если очередь пустая, то .peek() должен вернуть None.
.count() — должен возвращать количество элементов в очереди.
.clear() — должен очищать очередь.

Также добавьте в очередь контроль размера.

Если очередь полностью заполнена, 
    то очередной вызов .enqueue() должен возбудить исключение OverflowError.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.size = size
        self.length = 0

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)
        
        if self.length == self.size:
            raise OverflowError

        # Связываем новый элемент со следующим и с top.
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top

        # Связываем top с новым.
        self.top.next_node = new_node

        # Устанавливаем first, если это первая вставка.
        if not self.first:
            self.first = new_node
            
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """

        # Если элемент есть, то получаем его значение.
        if self.first:
            value = self.first.value

            # Смещаем указатель.
            self.first = self.first.prev_node

            # Удаляем последний элемент.
            self.first.next_node = None

            # Проверяем, не ссылается ли first на top.
            # Если ссылается, то сбрасываем first.
            if self.first.value is None:
                self.first = None

            self.length -= 1
            return value

        return None

    def count(self):
        """
        Возвращает количество элементов в очереди.
        """
        return self.length

    def peek(self):
        """
        Возвращает значение первого элемента очереди без его извлечения.
        """
        if not self.first:
            return
        
        return self.first.value

    def clear(self):
        """
        Очищает очередь.
        """
        self.length = 0
        self.first = None
        self.top.next_node = None


queue = Queue(3)

queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)

print(queue.dequeue())

print(queue.count())

queue.clear()
print(queue.count())

print(queue.peek())
