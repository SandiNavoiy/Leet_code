class Solution:
    def totalMoney(self, n: int) -> int:
        """Посчитать деньги в Leetcode Bank"""
        bal = 0
        days = 1
        wwek = 0

        for i in range(1, n+1):
            bal = bal + (days + wwek)
            days += 1
            if i%7 ==0:
                wwek += 1
                days = 1
        return bal

n = 10

s = Solution()
print(s.totalMoney(n))
