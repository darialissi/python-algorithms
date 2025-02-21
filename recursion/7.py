"""
Напишите функцию clear_brackets(), 
    которая принимает произвольную строку, содержащую скобки, 
        а затем удаляет из неё все незакрытые скобки вместе с их содержимым, если после них нет закрытых блоков
"""

def clear_brackets(string):
    if len(string) == 1:
        if string == "(":
            return ""
        
        return string
    
    if string[0] == "(":
        start = 1

        while start < len(string):
            if string[start] == ")":
                return string[:start] + clear_brackets(string[start:])
            start += 1

        return ""

    return string[0] + clear_brackets(string[1:])


def clear_brackets(string):
    """
    Упрощенный вариант
    """

    right = string.rfind("(")
    left = string.rfind(")")

    if right != -1 and right > left:
        string = clear_brackets(string[:right])
    return string


print(clear_brackets("abcde((abc"))
print(clear_brackets("abcde((abcd)("))
print(clear_brackets("abcde((abcd)(abcd"))