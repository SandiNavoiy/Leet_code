class Solution:
    def equalFrequency(self, word: str) -> bool:
        l = len(word)
        for c in range(l):
            target = word[:c] + word[c + 1 :]
            if len(set(target)) == len(set(multimode(target))):
                return True
        return False


word = "aazz"
s = Solution()
print(s.equalFrequency(word))
