"""
Напишите функцию digital_root(), которая принимает целое число и находит его цифровой корень.

Цифровой корень числа – это сумма всех цифр, которые составляют это число.

Если полученная сумма содержит более одной цифры, 
    то необходимо сложить цифры суммы и повторять операцию до тех пор, пока не останется одна цифра.
"""

def digital_root(num):
    if num < 10:
        return num

    return digital_root(num % 10 + num // 10)


root = digital_root(9999999)
print(root)