import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = dict(collections.Counter(word1))
        w2 = dict(collections.Counter(word2))
        for bukva in w1.keys():
            if bukva in w2:
                if abs(w1[bukva] - w2[bukva]) > 3:
                    return False
            else:
                if w1[bukva] > 3:
                    return False
        for bukva in w2.keys():
            if bukva not in w1 and w2[bukva] > 3:
                return False
        return True


word1 = "aaaa"
word2 = "bccb"
s = Solution()
print(s.checkAlmostEquivalent(word1, word2))
