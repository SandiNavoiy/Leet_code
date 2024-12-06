def is_valid_sequence(s):
    # Создаем словарь для соответствия открывающих и закрывающих скобок
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in brackets:  # Если символ — открывающая скобка
            stack.append(char)
        elif char in brackets.values():  # Если символ — закрывающая скобка
            if not stack or brackets[stack.pop()] != char:  # Проверяем соответствие
                return "NO"

    return (
        "YES" if not stack else "NO"
    )  # Если стек пуст, то последовательность правильная


# Пример ввода
input_string = input()
print(is_valid_sequence(input_string))
