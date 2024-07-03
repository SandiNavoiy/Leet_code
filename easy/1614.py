class Solution:
    def maxDepth(self, s: str) -> int:
        ''''''
        t = 0
        rez = 0
        for i in s:
            if i == "(":
                rez = rez + 1
            elif i == ")":
                rez = rez - 1

            t = max(t, rez)
        return t


s = "(1+(2*3)+((8)/4))+1"

sol = Solution()
print(sol.maxDepth(s))
