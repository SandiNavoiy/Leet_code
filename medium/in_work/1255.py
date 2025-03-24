class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        """"""
        a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        d = {i:j for i,j in zip(a, score)}
        rez = []
        print(d)

        for i in words:
            temp = 0
            for j in i:
                if d[j] !=0:
                    temp += d[j]
                else:
                    temp = 0
                    break
            if temp !=0:
                print(i)
                rez.append(temp)


        return rez

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

s = Solution()
print(s.maxScoreWords(words, letters, score))