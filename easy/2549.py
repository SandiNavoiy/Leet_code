class Solution:
    def distinctIntegers(self, n: int) -> int:
        """"""
        if n > 1:
            return n - 1
        else:
            return 1


n = 5
s = Solution()
print(s.distinctIntegers(n))
