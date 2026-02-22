class Solution:
    def mirrorDistance(self, n: int) -> int:
        """Зеркальное расстояние целого числа"""
        return abs(n - int(str(n)[::-1]))


s = Solution()
print(s.mirrorDistance(25))
