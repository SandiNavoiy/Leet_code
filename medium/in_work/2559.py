class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """"""
        glass = ("a", "e", "i", "o", "u")
        rez = []
        for i in words:
            if i[0] in glass and i[-1] in glass:
                rez.append(1)
            else:
                rez.append(0)

        ans = []
        for i in queries:
            ans.append(rez[i[0] : i[1] + 1].count(1))
        return ans


words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
s = Solution()
print(s.vowelStrings(words, queries))
