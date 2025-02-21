"""
Создайте функцию find(), которая будет искать значение в дереве с произвольным количеством потомков. 
Функция должна принимать корневой элемент дерева, а также ключ поиска. 
По результату функция должна возвращать значение, связанное с этим ключом. 

O(N).
"""

def find(node, key):
    if node.key == key:
        return node.value
    
    for child in node.children:
        value = find(child, key)

        if value is not None:
            return value

class Node:
    """
    Класс узла дерева.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []


root = Node("a", "A")
node_b = Node("b", "B")
node_c = Node("c", "C")
node_d = Node("d", "D")
node_i = Node("i", "I")

root.children.extend([node_b, node_c, node_d])
node_b.children.extend([Node("e", "E")])
node_c.children.extend([Node("f", "F"), Node("g", "K")])
node_d.children.extend([Node("h", "H"), node_i, Node("k", "K")])
node_i.children.extend([Node("l", "L"), Node("m", "M"), Node("n", "N"), Node("o", "O")])


result = find(root, 'm')
print(result)