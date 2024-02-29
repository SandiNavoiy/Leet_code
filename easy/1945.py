class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """"""
        alf = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
               "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
               "x": 24, "y": 25, "z": 26}
        temp = ""
        for i in s:
            if i in alf:
                temp = temp + str(alf[i])
        number = int(temp)
        ind = 0

        while ind < k:
            number_str = str(number)
            x = 0
            for i in number_str:
               x= x + int(i)

            number = x
            ind += 1
        return x



s = "iiii"
k = 1
sol = Solution()
print(sol.getLucky(s, k))
