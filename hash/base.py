"""
Поиск или добавление/удаление элемента O(N/B)
    :N - количество элементов
    :B - количество бакетов

    O(1) - оптимально

Рехэширование O(N)
"""

"""
Прямое связывание (на основе связных списков)
"""
class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[{self.key}:{self.value}]"


class HashTable:
    def __init__(self, size):
        """
        Создаем массив и заполняем его связными списками.
        """
        self.size = size
        self.elements = 0

        # Заполняем пустой ячейкой (вершиной связного списка).
        self.buckets = [Cell(None, None, None) for i in range(self.size)]

    def _hash(self, key):
        """
        Вычисляем хэш (индекс элемента массива).
        """
        return key % self.size

    def _find_cell_before(self, key):
        """
        Возвращает элемент связного списка, который стоит до искомого.
        Или None если искомого элемента нет.
        """

        # Получаем индекс элемента массива, используя хэширование.
        bucket_num = self._hash(key)
        # Получаем вершину подходящего связного списка.
        top = self.buckets[bucket_num]

        # Ищем элемент связного списка по ключу.
        cell = top
        while cell.next is not None:
            if cell.next.key == key:
                # Возвращаем предшествующий элемент.
                return cell
            cell = cell.next

        # Если элемента нет, то возвращаем None.
        return None

    def get(self, key):
        """
        Возвращает элемент по его ключу.
        Или None если элемента нет.
        """

        # Получаем элемент предшествующий искомому.
        cell_before = self._find_cell_before(key)

        if cell_before is None:
            return None

        # Возвращаем ячейку связного списка.
        return cell_before.next

    def insert(self, key, value):
        """
        Вставляем новое значение в хэш-таблицу.
        """

        # Ищем значение в хэш-таблице, если оно уже есть, то вызываем исключение.
        if self.get(key) is not None:
            raise ValueError("Ключ {key} уже находится в хэш-таблице.".format(key=key))

        # Получаем подходящий связный список для вставки нового элемента.
        bucket_num = self._hash(key)
        linked_list = self.buckets[bucket_num]

        # Добавляем новую ячейку в начало связного списка.
        new_cell = Cell(key, value, linked_list.next)
        linked_list.next = new_cell

        # Увеличиваем счетчик элементов хэш-таблицы.
        self.elements += 1

    def delete(self, key):
        """
        Удаляет элемент из хэш-таблицы по ключу.
        Возбуждает исключение, если элемента в хэш-таблице нет.
        """

        # Получаем элемент, который стоит перед тем, который нужно удалить.
        cell_before = self._find_cell_before(key)

        # Если такого нет, то возбуждаем исключение.
        if cell_before is None:
            raise ValueError(f"Ключа {key} нет в хэш-таблице.")

        # Удаляем элемент из связного списка.
        cell_before.next = cell_before.next.next

        # Обновляем количество элементов в хэш-таблице.
        self.elements -= 1
        return None

    def __str__(self):
        """
        Возвращает текстовое представление хэш таблицы.
        """
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}:"
            cell = cell.next
            while cell is not None:
                text += f" {cell}"
                cell = cell.next
            text += "\n"
        return text

ht = HashTable(10)

for key, value in map(lambda x: [int(x[1:4]), x],
                      ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                       "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                       "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                       "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                       "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS"]):
    ht.insert(key, value)

print(ht)

"""
Открытая адресация (линейное пробирование).

При удалении ячейка маркируется, далее поиск учитывает эту ячейку, 
    а при вставке новый элемент может занять позицию удаленного.
"""

class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"

    def delete(self):
        self.deleted = True
        self.key = None
        self.value = None


class HashTable:
    STEP = 1

    def __init__(self, size):
        self.size = size
        self.elements = 0
        # Создаем хэш-таблицу и заполняем её None.
        self.table = [None for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key, value):
        """
        Добавляем элемент в хэш-таблицу.
        Возбуждаем исключение, если элемент уже есть в таблице.
        """

        # Проверяем заполненность хэш-таблицы.
        if self.elements == self.size:
            raise OverflowError

        # Расчитываем начальный индекс для вставки.
        probe = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if self.table[probe] is None or self.table[probe].deleted:
                # Вставляем элемент в хэш-таблицу.
                self.table[probe] = DataItem(key, value)
                self.elements += 1
                return

            # Проверяем, нет ли элемента с переданным ключом в таблице.
            if self.table[probe].key == key:
                raise ValueError(f"Ключ {key} уже находится в таблице под индексом {probe}.)")

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def find(self, key):
        """
        Ищет элемент по ключу.
        Возвращает None если элемента нет в таблице.
        """
        probe = self._hash(key)
        num_probes = 0

        while True:
            num_probes += 1

            # Проверяем, не пуст ли очередной элемент.
            if self.table[probe] is None:
                return None

            # Проверяем, не находится ли в ячейке целевой элемент.
            if self.table[probe].key == key and not self.table[probe].deleted:
                return self.table[probe]

            # Проверяем, не прошли ли мы уже по кругу.
            if num_probes == self.size:
                return None

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def delete(self, key):
        """
        Удаляем элемент из хэш-таблицы.
        """
        item = self.find(key)
        if item:
            self.elements -= 1
            item.delete()

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.table[i] is None:
                text += f"{i: 3d}: [--------]\n"
            elif self.table[i].deleted:
                text += f"{i: 3d}: deleted\n"
            else:
                text += f"{i: 3d}: {self.table[i]}\n"

        return text


ht = HashTable(5)

for key, value in map(lambda x: [int(x[1:4]), x],
                      ["B617KM39RUS", "B398AB39RUS", "C254HE39RUS", "E123OK39RUS", "H637EA39RUS"]):
    ht.add(key, value)

print(ht)

ht.delete(617)
ht.delete(637)
print(ht)

ht.add(557, "H557OP39RUS")
print(ht)