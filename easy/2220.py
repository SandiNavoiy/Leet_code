class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """"""
        rez = 0
        x = bin(start)[2:]
        y = bin(goal)[2:]
        if len(x) > len(y):
            y = "0" * (len(x) - len(y)) + y
        elif len(y) > len(x):
            x = "0" * (len(y) - len(x)) + x
        for i in range(len(x)):
            if x[i] != y[i]:
                rez += 1

        return rez


start = 10
goal = 7
s = Solution()
print(s.minBitFlips(start, goal))
