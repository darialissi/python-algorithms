
from collections import deque

"""
Бинарное дерево.
Алгоритмы обхода дерева. O(N).
"""

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

root = BinaryNode(8)
node1 = BinaryNode(3)
node2 = BinaryNode(10)
node3 = BinaryNode(2)
node4 = BinaryNode(6)
node5 = BinaryNode(9)
node6 = BinaryNode(11)
node7 = BinaryNode(1)
node8 = BinaryNode(4)
node9 = BinaryNode(7)

root.left_child = node1
root.right_child = node2
node1.left_child = node3
node1.right_child = node4
node2.left_child = node5
node2.right_child = node6
node3.left_child = node7
node4.left_child = node8
node4.right_child = node9


def direct(node):
    """ Прямой обход """
    print(node.value, end="  ")
    if node.left_child:
        direct(node.left_child)
    if node.right_child:
        direct(node.right_child)


def symmetric(node):
    """ Симметричный обход """
    if node.left_child:
        symmetric(node.left_child)
    print(node.value, end="  ")
    if node.right_child:
        symmetric(node.right_child)


def reverse(node):
    """ Обход в обратном порядке """
    if node.left_child:
        reverse(node.left_child)
    if node.right_child:
        reverse(node.right_child)
    print(node.value, end="  ")


def wide(root):
    """ Обход в ширину """

    # Создаем очередь для хранения дочерних вершин.
    children = deque()

    children.append(root)

    # Обрабатываем очередь пока она не станет пустой.
    while children:
        node = children.popleft()

        print(node.value, end="  ")

        # Добавляем дочерние вершины в очередь.
        if node.left_child:
            children.append(node.left_child)
        if node.right_child:
            children.append(node.right_child)