class Solution:
    def reinitializePermutation(self, n):
        ans, perm, total = [i for i in range(n)], [i for i in range(n)], 0

        while total == 0 or perm != ans:
            perm = [
                perm[i // 2] if i % 2 == 0 else perm[n // 2 + (i - 1) // 2]
                for i in range(n)
            ]
            total += 1

        return total


n = 4
s = Solution()
print(s.reinitializePermutation(n))
