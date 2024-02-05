import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        """"""
        # Проверка длины пароля
        if len(password) < 8:
            return False

        # Проверка наличия строчной буквы
        if not re.search("[a-z]", password):
            return False

        # Проверка наличия заглавной буквы
        if not re.search("[A-Z]", password):
            return False

        # Проверка наличия цифры
        if not re.search("[0-9]", password):
            return False

        # Проверка наличия специального символа
        if not re.search("[!@#$%^&*()+-]", password):
            return False

        # Проверка отсутствия двух одинаковых символов подряд
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False

        # Если все проверки пройдены, пароль считается надежным
        return True


password = "-Aa1a1a1"
s = Solution()
print(s.strongPasswordCheckerII(password))
