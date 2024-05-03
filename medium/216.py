import itertools


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """"""
        rez = []
        if n < 10:
            new = [i for i in range(1, n + 1)]
        else:
            new = [i for i in range(1, 10)]

        comb = itertools.combinations(new, k)
        rez = [c for c in comb if sum(c) == n]

        return rez


k = 3
n = 7
s = Solution()
print(s.combinationSum3(k, n))
