class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        """"""
        ss = 0
        for i in words1:
            if i in words2 and words1.count(i) == 1 and words2.count(i) == 1:
                ss = ss + 1
        return ss


word1 = ["a", "ab"]
words2 = ["a", "a", "a", "ab"]

s = Solution()
print(s.countWords(word1, words2))
