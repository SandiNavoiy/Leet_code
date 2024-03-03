class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """"""
        if s == s[::-1]:
            return 1
        else:
            return 2


s = "abb"
sol = Solution()
print(sol.removePalindromeSub(s))
