from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new = []
        """"""
        x = dict(Counter(s))
        for i in order:
            if i in s:
                new.append(i * x[i])
                x[i] = 0
        for k, v in x.items():
            if v > 0:
                new.append(k * v)

        return "".join(new)


order = "cba"
s = "abcd"
sol = Solution()
print(sol.customSortString(order, s))
