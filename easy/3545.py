from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        """Минимальное количество удалений для не более K различных символов"""
        #вычисляем частоты символов

        counts = dict(Counter(s))
#сортируем, снасала символы с нименьшеми чатотами, меньше удалять
        counts = dict(sorted(counts.items(), key=lambda x: x[1]))
        #вычисляем разнику от требуемого
        d = len(counts) - k
#задаем счетчик
        rez = 0
        #если символов меньше чем требуемое то сразу выдаем 0
        if d <= 0:
            return rez
        #если не начинаем подсчет с насала частотного списка
        else:
            for i in counts.values():
                rez = rez + i
                d = d - 1
                if d == 0:
                    return rez


d = Solution()
print(d.minDeletion(s="abc", k=2))
