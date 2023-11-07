class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Merge Strings Alternately"""
        s_new = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                s_new = s_new + word1[i] + word2[i]
            return s_new
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                s_new = s_new + word1[i] + word2[i]

            return s_new + word1[len(word2) : :]
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                s_new = s_new + word1[i] + word2[i]

            return s_new + word2[len(word1) : :]


word1 = "ab"
word2 = "pqrs"
s = Solution()
print(s.mergeAlternately(word1, word2))
# "apbqrs"
