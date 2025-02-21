"""
Создайте рекурсивную функцию sum_num(), 
    которая принимает целое число N, а затем возвращает сумму всех чисел от 1 до N. 

Например, если число N=4, то нужно считать так: 1 + 2 + 3 + 4 = 10.
"""

def sum_num(num):
    if num <= 1:
        return num
    
    return num + sum_num(num - 1)


result = sum_num(4)
print(result)