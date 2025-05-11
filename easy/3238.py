class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        """Найдите количество победителей"""
        rez = 0

        d = {}
        for i in range(n):
            d[i] = []

        for i in pick:
            d[i[0]].append(i[1])

        for k, v in d.items():
            for i in v:
                if v.count(i) > k:
                    rez = rez + 1
                    break

        return rez


s = Solution()
print(s.winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]))
