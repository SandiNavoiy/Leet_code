class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        """Подсчет слов с заданным префиксом"""
        ss = 0
        for i in words:
            if pref in i[0 : len(pref)]:
                ss += 1

        return ss


words = ["pay", "attention ", "practice", "attend "]
pref = "at"
s = Solution()
print(s.prefixCount(words, pref))
