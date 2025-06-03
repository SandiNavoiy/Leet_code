class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        """"""
        x = p.split("*")
        first = s.find(x[0])
        if first == -1:
            return False
        second = s.rfind(x[1])
        if second == -1:
            return False
        if second > first:
            return True
        else:
            return False


s = "leetcode"
p = "ee*e"
sol = Solution()
print(sol.hasMatch(s, p))
