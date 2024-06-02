from itertools import groupby


class Solution:
    def compress(self, chars: list[str]) -> int:
        """"""
        s = []

        for key, group in groupby(chars):
            s.append(key)
            n = len(list(group))
            if n > 1:
                for i in str(n):
                    s.append(i)

        chars[:] = s

        return chars


chars = ["a", "a", "b", "b", "c", "c", "c"]
s = Solution()
print(s.compress(chars))
