class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """"""
        start = 0
        end = int(c**0.5)
        while start <= end:
            if start**2 + end**2 == c:
                return True
            elif start**2 + end**2 > c:
                end = end - 1
            elif start**2 + end**2 < c:
                start = start + 1

        return False


c = 2
s = Solution()
print(s.judgeSquareSum(c))
