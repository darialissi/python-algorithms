"""
Измените функцию gen_prime() так, чтобы она не обрабатывала четные числа. 
Такое улучшение должно уменьшить список l в два раза и почти в 2 раза сократить количество операций.

Используйте оптимизированную gen_prime() для создания программы, которая выводит список простых чисел от 2 до n, разделенных пробелом.
"""

def gen_prime(n):
    """
    Функция для генерации простых чисел в диапазон [2, N],
    используя решето Эратосфена.
    """
    # Создаем булев список длиной N / 2.
    # True - значит число простое, False - составное.
    l = [True] * (n // 2 + 1)

    # Результирующий список простых чисел.
    # Сразу ставим 2.
    result = [2]

    # Начальное значение
    p = 3

    # Начинаем перебирать все числа.
    while p <= n:
        # Вычисляем реальный индекс
        i = p // 2

        if l[i]:
            # Добавляеем очередное простое число.
            result.append(p)

            # Проход вперед для отметки чисел кратных p.
            factor = 2  # Множитель
            p_mult = p * factor  # Число кратное p.

            # Проходим по всем кратным числам и отмечаем их как False.
            while p_mult <= n:

                # Обработка только нечетных чисел.
                if p_mult % 2 == 1:
                    l[p_mult // 2] = False

                factor += 1
                p_mult = p * factor

        p += 2

    return result


print(gen_prime(21))