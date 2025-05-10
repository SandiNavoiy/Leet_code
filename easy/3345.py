from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """Наименьшая делимая цифра произведения I"""

        while True:
            s = [int( i) for i in str(n)]
            ddd = reduce(lambda x, y: x*y, s, 1)
            if ddd%t==0:
                return n
            else:
                n = n +1



s = Solution()
print(s.smallestNumber(10,2))