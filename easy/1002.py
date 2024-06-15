from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """Найдите общих персонажей"""
        d = Counter(words[0])
        rez = []

        for i in words:
            temp = Counter(i)
            d = d & temp
        for k, v in d.items():
            rez = rez + [k] * v

        return rez


word = ["bella", "label", "roller"]
s = Solution()
print(s.commonChars(word))
