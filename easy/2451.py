class Solution:
    def oddString(self, words: list[str]) -> str:
        """"""
        new = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25,
        }
        arr = []

        for i in words:
            temp = []
            for j in range(1, len(i)):
                temp.append(new[i[j]] - new[i[j - 1]])
            arr.append(temp)

        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                return words[i]


word = ["adc", "wzy", "abc"]
s = Solution()
print(s.oddString(word))
