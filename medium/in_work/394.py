class Solution:
    def decodeString(self, s: str) -> str:
        """"""
        stack = ""
        flag = 0
        rez = ""
        x = []
        y = []
        for i in s:
            if i == "[":
                flag = 1
            elif flag == 0:
                x.append(int(i))

            elif i == "]":
                y.append(stack)
                stack = ""
                flag = 0
            elif flag == 1:
                stack = stack + i
        for j in range(len(y)):
            rez = rez + y[j] * x[j]

        return rez


s = "2[abc]3[cd]ef"
sol = Solution()
print(sol.decodeString(s))
