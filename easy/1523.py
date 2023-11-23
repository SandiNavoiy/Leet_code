class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """Подсчет нечетных чисел в интервальном диапазоне"""
        new = 0
        if low == high:
            return int(low % 2 != 0)
        for i in range(low,high + 1):
            if i % 2 != 0:
                new += 1

        return new


low = 11
high = 11

s = Solution()
print(s.countOdds(low, high))


