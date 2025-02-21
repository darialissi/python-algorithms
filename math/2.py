"""
Взаимно простые числа — целые числа, не имеющие никаких общих делителей, кроме 1.
    :1 - числа взаимно простые
    :0 - числа не взаимно простые
    
Используем НОД.
"""

def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(a, b):
    if gcd_iter(a, b) == 1:
        return 1
    return 0


print(is_prime(13, 14))
print(is_prime(26, 14))