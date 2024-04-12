class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ''''''
        return n in [3**x for x in range(20)]
n = 27
s = Solution()
print(s.isPowerOfThree(n))