"""
Добавьте метод .insert() для вставки элементов в назначенное место связного списка.

Метод должен принимать два аргумента: 
    : value — значение вставляемого элемента
    : after_value — значение, после которого нужно добавить новый элемент

Если значения, после которого надо добавить элемент в списке не существует,
                                                то добавлять новый элемент не надо.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node(None)

    def append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        """

        # Перебираем поочереди все элементы, чтобы найти последний
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(value)

    def insert(self, value, after_value):
        """
        Вставка нового элемента в середину связного списка.
        После значения after_value
        """
        current = self.top
        
        while current:
            if current.value == after_value:
                node = Node(value)
                node.next_node = current.next_node
                current.next_node = node
                return
                
            current = current.next_node

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    

lst = List()

lst.append(1)
lst.insert(2, 1)
lst.insert(3, 2)
lst.insert(7, 5) # 5 в списке нет, значит 7 не будет добавлена

print(lst.__str__())