from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """"""
        c = dict(Counter(words))
        rez = []
        new = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        print(new)
        for i in range(k):
            rez.append(new[i][0])

        return rez


word = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
s = Solution()
print(s.topKFrequent(word, k))
