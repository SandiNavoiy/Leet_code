from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """"""
        c = 0
        s1 = Counter(s)
        t1 = Counter(t)
        print(t1)
        print(s1)

        return sum((t1 - s1).values())


s = "bab"
t = "aba"
sol = Solution()
print(sol.minSteps(s, t))
