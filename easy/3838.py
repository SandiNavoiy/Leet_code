class Solution:
    def mapWordWeights(self, words, weights) -> str:
        ''''''
        rez = []
        alf = {25: "a", 24: "b", 23: "c", 22: "d", 21: "e", 20: "f", 19: "g", 18: "h", 17: "i", 16: "j", 15: "k", 14: "l", 13: "m", 12: "n", 11: "o", 10: "p", 9: "q", 8: "r", 7: "s", 6: "t", 5: "u", 4: "v", 3: "w", 2: "x", 1: "y", 0: "z"}

        for word in words:
            t = 0
            for i in word:
                t += weights[ord(i) - 97]
            rez.append(t%26)
        s = ""

        print(rez)
        for i in rez:

            s += (alf[i])





        return s

s = Solution()
print(s.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
