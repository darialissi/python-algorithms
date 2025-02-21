"""
Тест простоты
    :1 - число простое
    :0 - число не простое
    
Используйте истинный тест простоты 
    с перебором всех возможных множителей от 2 до корня из N.
"""

def is_prime(num):

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
        
    return 1


print(is_prime(2243))
print(is_prime(2))