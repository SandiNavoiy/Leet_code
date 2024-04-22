class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        ans = bin(n)[2:]
        res = int(ans[::-1], 2)
        if ans == res:
            return True
        else:
            return False


n = 9
s = Solution()
print(s.isStrictlyPalindromic(n))
