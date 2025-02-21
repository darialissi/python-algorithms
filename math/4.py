"""
Праймориал числа N — это последовательное произведение простых чисел, меньших или равных N.

Например для расчета праймориала 12, нужно перемножить все простые числа, каждое из которых меньше или равно 12.

За основу возьмите код функции для решета Эратосфена.
"""

def gen_prime(n):
    """
    Функция для генерации простых чисел в диапазон [2, N],
    используя решето Эратосфена.
    """
    # Создаем булев список длиной N.
    # True - значит число простое, False - составное.
    l = [True] * (n + 1)

    # Результирующее произведение простых чисел.
    result = 1

    # Начальное значение
    p = 2

    # Начинаем перебирать все числа.
    while p <= n:

        if l[p]:
            result *= p

            # Проход вперед для отметки чисел кратных p.
            factor = 2  # Множитель
            p_mult = p * factor  # Число кратное p.

            # Проходим по всем кратным числам и отмечаем их как False.
            while p_mult <= n: 
                l[p_mult] = False
                factor += 1
                p_mult = p * factor

        p += 1

    return result


print(gen_prime(12))