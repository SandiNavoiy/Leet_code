from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """"""
        if s == s[::-1]:
            return len(s)
        chet = 0
        nechet = 0
        new = dict(Counter(s))
        for k, v in new.items():
            if v % 2 == 0:
                chet = chet + v
            else:
                if v >= 3:
                    chet = chet + v - 1
                    nechet = 1
                else:
                    nechet = 1

        return chet + nechet


s = "bananas"
sol = Solution()
print(sol.longestPalindrome(s))
