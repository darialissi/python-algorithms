"""
Создайте очередь на базе статического массива. 
Класс для управления очередью должен называться Queue и содержать два метода: 
    .enqueue() для добавления новых значений и .dequeue() для извлечения элемента.

В случае если в очереди не осталось элементов, то .dequeue() должен вернуть None.

Если очередь полностью заполнена, то очередной вызов .enqueue() должен возбудить исключение OverflowError.
"""

class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size
        self.first = 0
        self.end = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Queue(Array):
    """
    Очередь на базе статического массива.
    """

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        if self.length == self.size:
            raise OverflowError
            
        self.data[self.end] = value 
        self.end = (self.end + 1) % self.size
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if not self.length:
            return
        
        value = self.data[self.first] 
        self.length -= 1
        self.first = (self.first + 1) % self.size
        return value
    

queue = Queue(3)

queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())