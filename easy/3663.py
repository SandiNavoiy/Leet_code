from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        """Найдите наименее часто встречающуюся цифру."""
        #находим частоты
        d = dict(Counter(str(n)))
        # сортируем сначала по частоте, потом по цифре
        d = sorted(d.items(), key=lambda x: (x[1], x[0]))
        #выводим первый результат
        return int(d[0][0])

s = Solution()
print(s.getLeastFrequentDigit(1553322))
