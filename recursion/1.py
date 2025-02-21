"""
Напишите функцию digits_sum(), 
    которая принимает один аргумент — целое число, а затем рекурсивно вычисляет сумму цифр, из которых оно состоит.
"""

def digits_sum(num):
    if num < 10:
        return num
    
    return num % 10 + digits_sum(num // 10) 


res = digits_sum(1532)
print(res)