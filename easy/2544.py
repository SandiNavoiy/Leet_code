class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """"""
        new = str(n)
        x = 0
        for i in range(len(str(new))):
            if i % 2 == 0:
                x = x + int(new[i])
            else:
                x = x - int(new[i])
        return x



n = 111

s = Solution()
print(s.alternateDigitSum(n))
