"""
Напишите рекурсивную функцию capitalization(), которая принимает три аргумента: 
    :вложенную сумму
    :годовой процент по вкладу
    :срок вклада в месяцах
    
Сумма и количество месяцев — целые числа, годовой процент может быть как целым, так и вещественным.

Функция должна возвращать сумму, которую получит пользователь по окончанию вклада.
Возвращаемая сумма должна быть целым числом.

В данной задаче мы рассматриваем ежемесячную капитализацию, то есть проценты начисляются каждый месяц.
"""

def capitalization(amount, percent, month):
    if not month:
        return int(amount)
    
    calc = amount * percent / 100 / 12
    return capitalization(amount + calc, percent, month-1)


money = capitalization(10000, 10, 2)
print(money)