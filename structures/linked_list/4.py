"""
Реализуйте метод .append() дополнительно с указателем tail. 
    O(1)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
            
        self.tail.next_node = new_node
        self.tail = new_node

    def __str__(self):
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    

lst = List()

lst.append(1)
lst.append(2)
lst.append(3)

print(lst.__str__())