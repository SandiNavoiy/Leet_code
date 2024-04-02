class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        """"""
        x = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
        new = []
        for i in s:
            new.append(widths[x[i]-1])
        a = 0
        b = 0
        temp = 0
        for i in range(len(new)):
            temp = temp + new[i]
            if temp > 100:
                a += 1
                temp = new[i]


        return [a+1, temp]





widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
sol = Solution()
print(sol.numberOfLines(widths, s))