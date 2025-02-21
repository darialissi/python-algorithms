"""
Тест простоты
    :1 - число простое
    :0 - число не простое

Используйте истинный тест простоты 
    с перебором всех возможных множителей от 2 до корня из N с пропуском четных делителей.
"""

def is_prime(num):
    if num <= 2:
        return 1
    
    if num % 2 == 0:
        return 0

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return 0
        
    return 1


print(is_prime(2243))
print(is_prime(2))
print(is_prime(3))