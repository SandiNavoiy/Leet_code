class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """"""
        x = []
        for i in operations:
            if i.isdigit():
                x.append(int(i))
            elif i == "C":
                x.pop(-1)
            elif i == "D":
                x.append(x[-1] * 2)
            elif i == "+":
                x.append(x[-1] + x[-2])
            elif "-" in i:
                x.append(int(i))
        return sum(x)


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
s = Solution()
print(s.calPoints(ops))
# [5, -2, -4, 9, 5, 14]
