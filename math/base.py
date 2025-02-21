"""
НОД
"""

# Итеративный вариант
def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a


# Рекурсивный вариант
def gcd_rec(a, b):
    if b:
        return gcd_rec(b, a % b)
    return a
