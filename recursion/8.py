"""
В языке Си есть функция atoi(), которая приводит строку, содержащую числа, к целому числу.
Напишите собственную рекурсивную реализацию данной функции.

Функция atoi() должна работать аналогично функции int() из Python.
"""

def atoi(string, num=0):
    if len(string) == 1:
        return int(string) + (num * 10)

    num = int(string[0]) + (num * 10)

    return atoi(string[1:], num)


result = atoi("4159")
print(result)