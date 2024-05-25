import collections


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """"""
        n, res = len(s), 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                c = dict(collections.Counter(s[i:j]))
                if max(c.values()) <= 2:
                    res = max(res, len(s[i:j]))

        return res


s = "bcbbbcba"
sol = Solution()
print(sol.maximumLengthSubstring(s))
