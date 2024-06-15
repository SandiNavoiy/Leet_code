class Solution:
    def isPalindrome(self, x: int) -> bool:
        """"""
        return str(x) == str(x)[::-1]


x = 121
s = Solution()
print(s.isPalindrome(x))
