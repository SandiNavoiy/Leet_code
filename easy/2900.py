class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """"""

        rez = []
        for i in range(len(words)):
            if i == 0:
                rez.append(words[i])
                continue
            if groups[i] != groups[i - 1]:
                rez.append(words[i])

        return rez


words = ["e", "a", "b"]
groups = [0, 0, 1]
s = Solution()
print(s.getLongestSubsequence(words, groups))
