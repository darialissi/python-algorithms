"""
Модифицируйте класс SortedList так, чтобы он добавлял элементы с сортировкой по убыванию.
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)


class SortedList:
    """
    Сортированный связный список.
    """

    def __init__(self):
        self.top = Node()
        self.bottom = Node(-1) # Предполагается вставка только положительных нод
        self.top.next_node = self.bottom

    def append(self, value):
        """
        Добавление нового элемента в сортированный однонаправленный список.
        Время работы O(N).
        """

        current = self.top

        # Находим ноду перед той, в которую будем вставлять новый элемент.
        while current.next_node.value > value:
            current = current.next_node

        node = Node(value)
        node.next_node = current.next_node
        current.next_node = node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None and current.value > -1:
            end = ", " if current.next_node and current.next_node.value > -1 else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    

lst = SortedList()

lst.append(2)
lst.append(1)
lst.append(3)

print(lst.__str__())