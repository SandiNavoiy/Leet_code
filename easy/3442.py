from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        """"""
        d  = Counter(s)

        max_c = 0
        min_c = 999999999999999999999999999999999
        max_nc = 0
        min_nc = 999999999999999999999999999999999
        for k, v in d.items():
            if v %2 == 0:

                min_c = min(min_c, v)
            else:
                max_nc = max(max_nc, v)



        return max_nc - min_c
s = "tzt"
sol = Solution()
print(sol.maxDifference(s))