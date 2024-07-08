def rotate_letter(letter: str, shift: int) -> str:
    """
    Функция сдвигает символ letter на shift позиций.

    Аргументы:
    letter (str): Одна английская буква в нижнем регистре.
    shift (int): Значение сдвига буквы. Может быть положительным или отрицательным.

    Возвращает:
    str: Новая буква после сдвига.
    """
    if not letter.islower() or len(letter) != 1:
        raise ValueError(
            "Параметр letter должен быть одной английской буквой в нижнем регистре."
        )

    # Приводим сдвиг к значению в пределах 0-25
    shift = shift % 26

    # Преобразуем букву в числовое значение (0-25), сдвигаем и обратно преобразуем в букву
    new_letter_code = ord(letter) - ord("a")  # преобразуем в число 0-25
    new_letter_code = (new_letter_code + shift) % 26  # сдвигаем и берем по модулю
    new_letter = chr(new_letter_code + ord("a"))  # обратно преобразуем в букву

    return new_letter


def caesar_cipher(phrase: str, key: int) -> str:
    """Шифр Цезаря"""
    encrypted_phrase = []

    for char in phrase:
        if char.isalpha():  # если символ является буквой
            encrypted_char = (
                rotate_letter(char.lower(), key)
                if char.islower()
                else rotate_letter(char.lower(), key).upper()
            )
            encrypted_phrase.append(encrypted_char)
        else:  # если символ является знаком пунктуации или пробелом
            encrypted_phrase.append(char)

    return "".join(encrypted_phrase)


print(caesar_cipher.__annotations__)
print(caesar_cipher.__doc__)
print(caesar_cipher("lost in the echo", 1))
