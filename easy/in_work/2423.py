from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        ''''''
        x = dict(Counter(word))
        minn = min(x.values())
        maxx = max(x.values())
        print(x.values().count(maxx))

        if word.count(maxx) == word.count(minn) + 1:
            return True
        return False

word = "aazz"
s = Solution()
print(s.equalFrequency(word))