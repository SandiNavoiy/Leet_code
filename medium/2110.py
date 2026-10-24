class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        """Количество периодов плавного снижения цены акций."""
        #начальное значение, учитываем последний элекмент, поэтому +1
        rez = 1
        #временная пеерменная. изначально 1 ибо 1 элемент это снижение
        temp = 1
#проходим по последовательности
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                temp += 1
            else:
                temp = 1
#обязатено тут. иначе хрень
            rez += temp

        return rez



s = Solution()

print(s.getDescentPeriods([3,2,1,4]))
