class Solution:
    def countValidWords(self, sentence: str) -> int:
        ''''''
        rez = []
        new  = []
        for i in sentence.split(' '):
            if i != "":
                new.append(i)
        for i in new:
            if i.isdigit():
                pass
            else:
                rez.append(i)

        return rez

sentence = "!this  1-s b8d!"
s  = Solution()
print(s.countValidWords(sentence))
