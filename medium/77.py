from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """"""
        temp = [i for i in range(1, n + 1)]
        x = list(combinations(temp, k))

        return x


n = 4
k = 2
s = Solution()
print(s.combine(n, k))
