from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        """"""
        x = dict(Counter(word))
        print(sum(x.values()))

        return x


word = "xycdefghij"
s = Solution()
print(s.minimumPushes(word))
