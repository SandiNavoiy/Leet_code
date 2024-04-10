from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ''''''
        new = []
        y = dict(Counter(target))
        x = dict(Counter(s))
        for i, j in y.items():
            if i in x:
                new.append(x[i]// y[i])
            else:
                return 0
        return min(new)
s = "abc"
target = "abcd"
sol = Solution()
print(sol.rearrangeCharacters(s, target))