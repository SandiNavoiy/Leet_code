from math import dist


class Solution:
    def validSquare(
        self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]
    ) -> bool:
        """"""
        a = dist(tuple(p1), tuple(p2))
        b = dist(tuple(p1), tuple(p3))
        c = dist(tuple(p1), tuple(p4))
        d = dist(tuple(p2), tuple(p3))
        e = dist(tuple(p2), tuple(p4))
        f = dist(tuple(p3), tuple(p4))
        if len({a, b, c, d, e, f}) == 2 and 0 not in {a, b, c, d, e, f}:
            return True
        else:
            return False


p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]
s = Solution()
print(s.validSquare(p1, p2, p3, p4))
