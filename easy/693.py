class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """"""
        x = bin(n)[2:]
        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                return False
        return True


n = 5
s = Solution()
print(s.hasAlternatingBits(n))
