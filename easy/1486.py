class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """"""
        res = 0
        for i in range(n):
            res = res ^ start + 2 * i

        return res


n = 5
start = 0
s = Solution()
print(s.xorOperation(n, start))
