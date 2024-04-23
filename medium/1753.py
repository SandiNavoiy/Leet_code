class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """"""
        new = [a, b, c]
        new.sort()
        ttt = 0
        while True:
            new[2] = new[2] - 1
            new[1] = new[1] - 1
            new.sort()
            ttt = ttt + 1

            if sum(new) == new[2]:
                return ttt

        return ttt


a = 81510
b = 13219
c = 14172
s = Solution()
print(s.maximumScore(a, b, c))
