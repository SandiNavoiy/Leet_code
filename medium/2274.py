from itertools import pairwise


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        rez = max((b - a - 1 for a, b in pairwise(special)), default=0)
        return max(rez, special[0] - bottom, top - special[-1])


bottom = 6
top = 8
special = [7, 6, 8]
s = Solution()
print(s.maxConsecutive(bottom, top, special))
