class Solution:
    def reorderSpaces(self, text: str) -> str:
        """"""
        new = []

        prob = text.count(" ")
        if prob == 0:
            return text
        x = text.split(" ")
        for i in x:
            if i != "":
                new.append(i)
        col_w = len(new)
        z = int(prob / (col_w - 1))
        rez = []
        for i in range(len(new)):
            rez.append(new[i])
            rez.append(" " * z)
        print((prob / (col_w - 1)) % 1)

        if (prob / (col_w - 1)) % 2 == 0:
            rez.pop(-1)
        else:
            rez.pop(-1)
            rez.append(" ")

        print(rez)

        return "".join(rez)


text = "a"
s = Solution()
print(s.reorderSpaces(text))
