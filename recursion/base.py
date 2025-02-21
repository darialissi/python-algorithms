"""
Переворот списка.
"""

def list_reverse(seq):
    """Итеративная функция"""
    for i in range(len(seq) // 2):
        el = seq[i]
        seq[i] = seq[len(seq) - 1 - i]
        seq[len(seq) - 1 - i] = el


def list_reverse_rec(seq, i=0):
    """Рекурсивная функция"""
    el = seq[i]
    seq[i] = seq[len(seq) - 1 - i]
    seq[len(seq) - 1 - i] = el

    if i < (len(seq) - 1) // 2:
        list_reverse_rec(seq, i+1)

"""
Факториал.
"""

def factorial_rec(n):
    """Рекурсивная функция"""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

"""
Фибоначчи.
"""

from functools import lru_cache

@lru_cache
def fib(n):
    """Рекурсивная функция"""
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)
