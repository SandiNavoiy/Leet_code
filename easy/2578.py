class Solution:
    def splitNum(self, num: int) -> int:
        """"""
        new = list(str(num))
        new.sort()
        x = [new[i] for i in range(len(new)) if i % 2 == 0]
        y = [new[i] for i in range(len(new)) if i % 2 != 0]
        return int("".join(x)) + int("".join(y))


num = 4325
s = Solution()
print(s.splitNum(num))
