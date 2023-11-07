class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """Проверьте, является ли предложение панграммой"""
        alf = "abcdefghijklmnopqrstuvwxyz"
        sum = 0
        for i in alf:
            if i in sentence:
                sum += 1

        print(sum)
        if sum == 26:
            return True
        else:
            return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
s = Solution()
print(s.checkIfPangram(sentence))
