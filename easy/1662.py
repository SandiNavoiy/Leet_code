class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """Проверьте, эквивалентны ли два массива строк"""
        w = "".join(word1)
        e = "".join(word2)
        if w == e:
            return True
        else:
            return False


word1 = ["ab", "c"]
word2 = ["a", "bc"]
s = Solution()
print(s.arrayStringsAreEqual(word1, word2))
