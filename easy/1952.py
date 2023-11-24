class Solution:
    def isThree(self, n: int) -> bool:
        """Три делителя"""
        cc = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cc += 1

        if cc == 3:
            return True
        else:
            return False


n = 2
s = Solution()
print(s.isThree(n))
