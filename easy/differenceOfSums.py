class Solution:
    """Разница делимых и неделимых сумм
"""
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(n +1 ):

            if i % m == 0:
                num2  = num2 + i
            else:
                num1 = num1 + i

        return (num1 - num2)

n = 5
m = 1
s = Solution()
print(s.differenceOfSums(n, m))

