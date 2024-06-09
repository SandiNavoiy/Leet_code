from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        ''''''
        right_count = Counter(s)
        left_count = Counter()
        num_splits = 0
        print(right_count)
        print(left_count)

        for char in s:
            # Перемещаем символ из правого словаря в левый
            left_count[char] += 1
            right_count[char] -= 1

            # Если символ больше не встречается в правой части, удаляем его
            if right_count[char] == 0:
                del right_count[char]

            # Проверяем количество уникальных символов в левой и правой частях
            if len(left_count) == len(right_count):
                num_splits += 1

        return num_splits



s = "aacaba"

sol = Solution()
print(sol.numSplits(s))