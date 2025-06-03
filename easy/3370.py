class Solution:
    def smallestNumber(self, n: int) -> int:
        """Наименьшее число со всеми установленными битами"""
        while True:
            if "0" not in bin(n)[2:]:
                return n
            else:
                n += 1


s = Solution()
print(s.smallestNumber(10))
