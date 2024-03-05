from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        """"""
        x = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if sqrt(i * i + j * j) <= n and sqrt(i * i + j * j) % 1 == 0:
                    x += 1

        return x


n = 5
s = Solution()
print(s.countTriples(n))
