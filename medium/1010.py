class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        """"""
        rez = 0
        x = [0] * 60
        for i in time:
            t = i % 60
            comp = (60 - t) % 60
            rez = rez + x[comp]
            x[t] = x[t] + 1
        return rez


time = [30, 20, 150, 100, 40]

s = Solution()
print(s.numPairsDivisibleBy60(time))
