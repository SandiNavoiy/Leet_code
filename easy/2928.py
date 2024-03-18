class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """"""
        new = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if (i + j + k) == n:
                        print(i, j, k)
                        new += 1
        return new


n = 5
limit = 2

s = Solution()
print(s.distributeCandies(n, limit))
