class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """Минимальная стоимость билетов"""
        # создаем мемо массив
        dp = [0] * 366
        # начинаем итерировать по дням, сравнивая то что есть в исходном дайс
        for i in range(len(dp)):
            # если дня нет повторяем предыдущее
            if i not in days:
                dp[i] = dp[i - 1]
                # если есть находим в обратную стоимость 1б7б30 дней обратно
            else:
                sold1 = dp[i - 1] + costs[0]
                sold7 = dp[max(i - 7, 0)] + costs[1]
                sold30 = dp[max(i - 30, 0)] + costs[2]
                # выбираем минимальне
                dp[i] = min(sold1, sold7, sold30)

        return dp[-1]


s = Solution()
print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
