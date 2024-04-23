class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """"""
        new = []
        for i in range(1, n + 1):
            if n % i == 0:
                new.append(i)
        new.sort()
        if len(new) < k:
            return -1

        return new[k - 1]


n = 4
k = 4
s = Solution()
print(s.kthFactor(n, k))
