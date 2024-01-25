class Solution:
    def generateTheString(self, n: int) -> str:
        """"""
        new = ""
        if n % 2 == 0:
            new = "a" * (n - 1) + "b"
            return new
        else:
            new = "a" * n
            return new


n = 4
s = Solution()
print(s.generateTheString(n))
