"""
Запрограммируйте в классе MorseTree() метод .insert_char() для формирования дерева Морзе. 
"""

class MorseBinaryNode:
    def __init__(self, char):
        self.char = char
        self.dot_child = None
        self.dash_child = None
        self.root = False

    def set_children(self, dot=None, dash=None):
        self.dot_child = dot
        self.dash_child = dash

    def __str__(self):
        return str(self.char)


class MorseTree:

    def __init__(self):
        self.morse = MorseBinaryNode(None)
        self.morse.root = True

    def insert_char(self, morse_code, char):
        """
        Вставляет символ char с кодом morse_code в дерево self.morse
        """
        path = self.morse

        for ch in morse_code:

            if ch == ".":
                if path.dot_child is None:
                    path.dot_child = MorseBinaryNode(None)

                path = path.dot_child

            elif ch == "-":
                if path.dash_child is None:
                    path.dash_child = MorseBinaryNode(None)

                path = path.dash_child

        # Перезаписываем значение последнего узла
        path.char = char


    def get_nodes(self, node=None, result=None):
        """
        Симметричный обход с выводом всех узлов.
        Не изменяйте этот метод, он нужен для тестирования.
        """

        if result is None:
            result = []
            node = self.morse

        if node.dot_child:
            self.get_nodes(node.dot_child, result)

        if not node.root:
            result.append(node.char)

        if node.dash_child:
            self.get_nodes(node.dash_child, result)

        return ",".join(map(lambda x: "" if x is None else x, result))
    

tree = MorseTree()

tree.insert_char(".-", "A")
tree.insert_char(".", "E")
tree.insert_char("..", "I")
tree.insert_char("--", "M")
tree.insert_char("-.", "N")
tree.insert_char("-", "T")

print(tree.get_nodes())