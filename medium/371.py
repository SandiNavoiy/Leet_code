from math import exp, log


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 and b != 0:
            return b
        elif b == 0 and a != 0:
            return a

        return int(log(exp(a) * exp(b)))


a = 2
b = 3
s = Solution()
print(s.getSum(a, b))
