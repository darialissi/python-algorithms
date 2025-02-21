"""
Модифицируйте код класса так, что в момент, 
    когда количество удаленных элементов будет превышать 30% от длины массива, произойдет рехэширование массива. 
        Элементы, которые имели deleted=True должны быть реально удалены.

Обратите внимание, что при рехэшировании элементы должны попадать в новую таблицу в том порядке, 
    в котором они хранились в старой таблице (self.table).
"""

class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        return f"[{self.key:02d}:{self.value}]"

    def delete(self):
        self.deleted = True
        self.key = None
        self.value = None


class HashTable:
    STEP = 1

    def __init__(self, size):
        self.size = size
        self.elements = 0
        self.deleted = 0

        self.table = [None for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key, value, item=None):
        """
        Добавляем элемент в хэш-таблицу.
        Возбуждаем исключение, если элемент уже есть в таблице.
        """

        # Проверяем заполненность хэш-таблицы.
        if self.elements == self.size:
            raise OverflowError

        # Рассчитываем начальный индекс для вставки.
        probe = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if self.table[probe] is None or self.table[probe].deleted:

                # Если это замена удаленного элемента, то уменьшаем их количество.
                if self.table[probe] is not None and self.table[probe].deleted:
                    self.deleted -= 1

                # Вставляем элемент в хэш-таблицу.
                self.table[probe] = item or DataItem(key, value)
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
            self.deleted += 1
            item.delete()
            
        if self.deleted / self.size > 0.3:
            self.change_size()

    def change_size(self):
        # Запоминаем старую таблицу (поверхностная копия)
        old_table = self.table.copy()

        # сбрасываем заполненность
        self.elements = 0
        self.deleted = 0

        # Создаём новую таблицу
        self.table = [None for _ in range(self.size)]

        # Заполняем новую таблицу (просто проходим по всем элементам старой таблицы
        for item in old_table:
            if item is not None and not item.deleted:
                # Вставляем в новую таблицу (без создания нового объекта)
                self.add(item.key, item.value, item)

        # Удаляем старую таблицу
        del old_table

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        values = []
        for i in range(self.size):
            if self.table[i] is None:
                values.append(f"EMPTY")
            elif self.table[i].deleted:
                values.append(f"DELETED")
            else:
                values.append(f"{self.table[i]}")

        return " ".join(values)
    

ht = HashTable(5)

ht.add(47, "A")
ht.add(13, "B")
ht.add(5, "C")
ht.add(15, "D")
ht.add(25, "E")

print(ht)

ht.delete(47)
print(ht)

# Удаляем второй элемент
# Количество удаленных элементов превышает 30% от общего размера массива -
# произойдет рехэширование
ht.delete(13)
print(ht)