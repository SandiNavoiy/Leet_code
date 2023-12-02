class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """Найдите общих персонажей"""
        if not words:
            return []

        myset = set(words[0])
        for word in words[1:]:
            myset = myset.intersection(set(word))

        return list(myset)


word = ["bella","label","roller"]
s = Solution()
print(s.commonChars(word))