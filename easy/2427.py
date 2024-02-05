class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """"""
        x = 0
        for i in range(1, max(a, b) + 1):
            if a % i == 0 and b % i == 0:
                x += 1

        return x


a = 25
b = 30
s = Solution()
print(s.commonFactors(a, b))
