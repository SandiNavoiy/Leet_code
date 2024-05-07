class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """"""
        new = sentence.split()
        if new[0][0] != new[-1][-1]:
            return False
        for i in range(1, len(new)):
            if new[i][0] != new[i - 1][-1]:
                return False
        return True


sentence = "leetcode exercises sound delightful"
s = Solution()
print(s.isCircularSentence(sentence))
