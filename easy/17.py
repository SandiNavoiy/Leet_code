class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Палиндром"""
        strrr = str(x)
        if strrr == strrr[: :-1]:
            return True
        else:
            return False


x = 12

s = Solution()
print(s.isPalindrome(x))