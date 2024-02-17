class Solution:
    def reformat(self, s: str) -> str:
        ''''''
        x = []
        y = []
        new = []
        for i in s:
            if i.isdigit():
                x.append(i)
            else:
                y.append(i)
        if len(x) == 0 or len(y) == 0:
            return ''
        elif len(x) - len(y) > 1 or len(y) - len(x) > 1:
            return ''
        elif len(x) > len(y):
            for i in range(len(y)):
                new.append(y[i])
                new.append(x[i])
            new.append(x[-1])
        elif len(y) > len(x):
            for i in range(len(x)):
                new.append(y[i])
                new.append(x[i])
            new.append(y[-1])
        else:
            for i in range(len(x)):
                new.append(y[i])
                new.append(x[i])

        return "".join(new)


s = "a0b1c2"
sol = Solution()
print(sol.reformat(s))