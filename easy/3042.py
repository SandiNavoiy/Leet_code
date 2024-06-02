class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """"""
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                print(words[i])
                print(words[j])
                print(words[j][0 : len(words[i])])
                print(words[j][len(words[j]) - len(words[i]) :])
                print("---")
                if (
                    words[i] == words[j][0 : len(words[i])]
                    and words[i] == words[j][len(words[j]) - len(words[i]) :]
                ):
                    pass


word = ["a", "aba", "ababa", "aa"]
s = Solution()
print(s.countPrefixSuffixPairs(word))
