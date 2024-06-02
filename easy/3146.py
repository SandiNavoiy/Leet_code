class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        """"""
        rez = 0
        for i in range(len(s)):
            rez = rez + abs(i - t.find(s[i]))
        return rez


s = "abc"
t = "bac"
sol = Solution()
print(sol.findPermutationDifference(s, t))
