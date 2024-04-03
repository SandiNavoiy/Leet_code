class Solution:
    def tribonacci(self, n: int) -> int:
        """"""
        dd = [0, 1, 1]
        for i in range(3, n + 1):
            dd.append(dd[i - 1] + dd[i - 2] + dd[i - 3])

        if n == 0:
            return dd[0]
        return dd[-1]


n = 25
s = Solution()
print(s.tribonacci(n))
