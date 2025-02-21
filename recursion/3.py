"""
Создайте рекурсивную функцию join(), которая принимает два аргумента:

    :строка-клей, которая будет соединять элементы массива
    :массив строк, которые нужно соединить

Функция должна склеить строки и вернуть результат.
"""

def join(clue, seq):
    if not seq:
        return ''
    
    if len(seq) == 1:
        return seq[0]
    
    return seq[0] + clue + join(clue, seq[1:])


result = join("-", ["alpha", "beta", "gamma"])
print(result)