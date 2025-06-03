class Solution:
    def maxProduct(self, n: int) -> int:
        """Максимальное произведение двух цифр"""

        arr = sorted([int(i) for i in str(n)])

        return arr[-1] * arr[-2]


s = Solution()
print(s.maxProduct(124))
