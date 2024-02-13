class Solution:
    def divisorGame(self, n: int) -> bool:
        ''''''
        if n % 2 == 0:
            return True
        else:
            return False


n = 10
s = Solution()
print(s.divisorGame(n))
