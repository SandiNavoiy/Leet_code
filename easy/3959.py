class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        """Проверка корректности целого числа."""
        ls = [int(i) for i in str(n)]
        ls1 = [int(i)**2 for i in str(n)]


        return sum(ls1) - sum(ls) >= 50





n = 1000
s = Solution()
print(s.checkGoodInteger(n))