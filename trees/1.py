"""
Одно из предназначений двоичных деревьев — это хранение символов для азбуки Морзе. 
В азбуке любая буква кодируется алфавитом, который содержит всего два символа (точку или тире).

Левый потомок узла такого дерева отвечает за точку, а правый за тире. 
Если взять код .--. и начать спуск по дереву, 
    каждый раз выбирая левую или правую сторону (точка или тире), то мы дойдём до символа "P".

Необходимо запрограммировать метод get_word() для формирования слова.
"""

class MorseBinaryNode:
    def __init__(self, char):
        self.char = char
        self.dot_child = None
        self.dash_child = None

    def set_children(self, dot=None, dash=None):
        self.dot_child = dot
        self.dash_child = dash

    def __str__(self):
        return str(self.char)


class MorseTree:

    def __init__(self):

        # Формируем двоичное дерево
        self.morse = MorseBinaryNode(None)

        # Заполняем рядами
        e = MorseBinaryNode("E")
        t = MorseBinaryNode("T")

        self.morse.set_children(e, t)

        i = MorseBinaryNode("I")
        a = MorseBinaryNode("A")
        n = MorseBinaryNode("N")
        m = MorseBinaryNode("M")

        e.set_children(i, a)
        t.set_children(n, m)

        s = MorseBinaryNode("S")
        u = MorseBinaryNode("U")
        r = MorseBinaryNode("R")
        w = MorseBinaryNode("W")
        d = MorseBinaryNode("D")
        k = MorseBinaryNode("K")
        g = MorseBinaryNode("G")
        o = MorseBinaryNode("O")

        i.set_children(s, u)
        a.set_children(r, w)
        n.set_children(d, k)
        m.set_children(g, o)

        h = MorseBinaryNode("H")
        v = MorseBinaryNode("V")
        f = MorseBinaryNode("F")
        uu = MorseBinaryNode("Ü")
        l = MorseBinaryNode("L")
        au = MorseBinaryNode("Ä")
        p = MorseBinaryNode("P")
        j = MorseBinaryNode("J")
        b = MorseBinaryNode("B")
        x = MorseBinaryNode("X")
        c = MorseBinaryNode("C")
        y = MorseBinaryNode("Y")
        z = MorseBinaryNode("Z")
        q = MorseBinaryNode("Q")
        ou = MorseBinaryNode("Ö")
        ch = MorseBinaryNode("CH")

        s.set_children(h, v)
        u.set_children(f, uu)
        r.set_children(l, au)
        w.set_children(p, j)
        d.set_children(b, x)
        k.set_children(c, y)
        g.set_children(z, q)
        o.set_children(ou, ch)

        d5 = MorseBinaryNode("5")
        d4 = MorseBinaryNode("4")
        d3 = MorseBinaryNode("3")
        d2 = MorseBinaryNode("2")
        d1 = MorseBinaryNode("1")
        d6 = MorseBinaryNode("6")
        d7 = MorseBinaryNode("7")
        d8 = MorseBinaryNode("8")
        d9 = MorseBinaryNode("9")
        d0 = MorseBinaryNode("0")

        h.set_children(d5, d4)
        v.dash_child = d3
        uu.dash_child = d2
        j.dash_child = d1
        b.dot_child = d6
        z.dot_child = d7
        ou.dot_child = d8
        ch.set_children(d9, d0)

    def get_char(self, morse_char):

        node = self.morse

        for i in morse_char:
            if i == ".":
                node = node.dot_child
            elif i == "-":
                node = node.dash_child
            else:
                raise ValueError(f"Неизвестный символ <{i}>")

        return node.char

    def get_word(self, morse_word):
        """
        Формируем слово.
        .--. -.-- - .... --- -. -> PYTHON
        """
        word = ""

        for morse_char in morse_word.split():
            word += self.get_char(morse_char)

        return word
    

morse = ".--. -.-- - .... --- -."
tree = MorseTree()
print(tree.get_word(morse))