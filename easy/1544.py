class Solution:
    def makeGood(self, s: str) -> str:
        """"""
        step = 0
        next_step = 1  # Изменено на 1, чтобы цикл while выполнился хотя бы один раз
        while step != next_step:  # Изменено условие для цикла
            step = len(s)
            i = 0
            while (
                i < len(s) - 1
            ):  # Использован цикл while вместо цикла for, чтобы корректно обрабатывать изменения в строке
                if (
                    abs(ord(s[i]) - ord(s[i + 1])) == 32
                ):  # Изменено условие для корректной проверки символов
                    s = (
                        s[:i] + s[i + 2 :]
                    )  # Использована операция среза для удаления символов из строки
                    i = max(
                        i - 1, 0
                    )  # Уменьшаем i на 1, чтобы проверить предыдущий символ
                else:
                    i += 1
            next_step = len(s)
        return s


s = "abBAcC"
sol = Solution()
print(sol.makeGood(s))
