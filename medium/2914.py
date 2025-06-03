class Solution:
    def minChanges(self, s: str) -> int:
        """Минимальное количество изменений, чтобы сделать двоичную строку красивой"""
        i = 0  # счетчик цикла
        count = 0  # счетчик изменений
        while i < len(s):
            if (
                s[i] != s[i + 1]
            ):  # если изменения надо, увеличиваем на 1. пройти надо все двойкм строки по порядку
                count += 1
            i += 2

        return count


s = "1001"

sol = Solution()
print(sol.minChanges(s))
