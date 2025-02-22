"""
Создайте функцию calc_nodes(), 
    которая будет обходить дерево и подсчитывать количество узлов в нём. 
"""

def calc_nodes(node):
    
    calc = 1

    for child in node.children:
        calc += calc_nodes(child)

    return calc


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

nodes = calc_nodes(root)
print(nodes)