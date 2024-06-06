class Solution:
    def maxProduct(self, words: list[str]) -> int:
        """"""
        max_len = 0
        new = []
        for i in words:
            new.append([set(i)])

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len


Words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
s = Solution()
print(s.maxProduct(Words))
