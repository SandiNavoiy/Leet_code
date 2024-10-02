class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """"""
        glass = ("a", "e", "i", "o", "u")
        rez = []
        rez = [1 if word[0] in glass and word[-1] in glass else 0 for word in words]
        # Вычисляем префиксные суммы
        prefix_sum = [0] * (len(rez) + 1)
        for i in range(len(rez)):
            prefix_sum[i + 1] = prefix_sum[i] + rez[i]

        ans = []
        for q in queries:
            ans.append(prefix_sum[q[1] + 1] - prefix_sum[q[0]])

        return ans


words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
s = Solution()
print(s.vowelStrings(words, queries))
