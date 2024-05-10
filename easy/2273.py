class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        """"""
        rez = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                rez.append(words[i])

        return rez


word = ["abba", "baba", "bbaa", "cd", "cd"]
s = Solution()
print(s.removeAnagrams(word))
