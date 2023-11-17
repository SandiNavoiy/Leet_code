class Solution:
    def isHappy(self, n: int) -> bool:
        """Счастливое число"""
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1


n = 19
s = Solution()
print(s.isHappy(n))
