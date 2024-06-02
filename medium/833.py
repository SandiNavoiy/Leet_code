class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Создаем список кортежей (индекс, источник, цель) и сортируем его по индексам
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])

        # Создаем список символов, чтобы было проще работать с изменениями
        s = list(s)

        # Проходим по отсортированным заменам в обратном порядке
        for i, src, tgt in replacements[::-1]:
            # Проверяем, совпадает ли подстрока в исходной строке с заменяемой подстрокой
            if s[i:i + len(src)] == list(src):
                # Заменяем подстроку на целевую строку
                s[i:i + len(src)] = list(tgt)

        # Возвращаем объединенную строку
        return ''.join(s)

# Пример использования
s = "abcdef"
indices = [2, 2]
sources = ["cdef", "feg"]
targets = ["feg", "abc"]
sol = Solution()
print(sol.findReplaceString(s, indices, sources, targets))  # Ожидаемый результат: "abfeg"
