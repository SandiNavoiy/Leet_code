class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """"""
        new = []
        for i in words:
            for j in words:
                if j in i and j != i:
                    new.append(j)

        return list(set(new))


word = ["leetcoder", "leetcode", "od", "hamlet", "am"]

s = Solution()
print(s.stringMatching(word))
