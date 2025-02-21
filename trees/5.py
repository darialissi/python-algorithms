"""
Создайте функцию get_sum(), 
    которая будет обходить дерево с произвольным количеством элементов 
        и суммировать все значения (value), которые хранятся в узлах дерева.
"""

def get_sum(node):

    result = node.value

    for child in node.children:
        result += get_sum(child)

    return result


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

root = Node(0)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(5)
node_4 = Node(4)

root.children.extend([node_1, node_2, node_3])
node_1.children.extend([Node(3)])
node_2.children.extend([Node(7), Node(1)])
node_3.children.extend([Node(0), node_4, Node(2)])
node_4.children.extend([Node(12), Node(4), Node(5), Node(8)])

result = get_sum(root)
print(result)