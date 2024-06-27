class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """Returns True"""
        new = {}
        for i, v in enumerate(order):
            new[v] = i
        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            flag = False
            min_range = min(len(word1), len(word2))
            for j in range(min_range):
                if new[word1[j]] > new[word2[j]]:
                    return False
                elif new[word1[j]] < new[word2[j]]:
                    flag = True
                    break
            if not flag and len(word1) > len(word2):
                return False
        return True


Words = ["kuvp", "q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
s = Solution()
print(s.isAlienSorted(Words, order))
