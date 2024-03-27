class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ''''''
        glass = ('a', 'e', 'i', 'o', 'u')
        new = sentence.split()
        for i in range(len(new)):
            if new[i][0].lower() in glass:
                new[i]  =new[i] + "ma" + "a"*(i+1)
            else:
                new[i] = new[i][1::] + new[i][0]+ "ma" + "a"*(i+1)

        return " ".join(new)
sentence = "I speak Goat Latin"
#"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
s= Solution()
print(s.toGoatLatin(sentence))