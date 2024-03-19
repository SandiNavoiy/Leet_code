import collections


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        """"""

        s1 = (s1 + " " + s2).split()
        new = dict(collections.Counter(s1))
        rez = []
        for j, i in new.items():
            if i == 1:
                rez.append(j)

        return rez


s1 = "это яблоко сладкое"
s2 = "это яблоко кислое"
s = Solution()
print(s.uncommonFromSentences(s1, s2))
