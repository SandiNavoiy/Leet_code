class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        """"""
        new = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if n == j + i and "0" not in str(i) and "0" not in str(j):
                    new.append(i)
                    new.append(j)
                    return new


n = 11
s = Solution()
print(s.getNoZeroIntegers(n))
