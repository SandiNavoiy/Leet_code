class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        """"""
        rez = 0
        for i in range(0, len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    rez = max(j - i, rez)
        return rez


colors = [1, 8, 3, 8, 3]
s = Solution()
print(s.maxDistance(colors))
