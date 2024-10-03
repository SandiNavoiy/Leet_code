class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        """"""
        # for i in range(2, num + 1):
        #    if i - 1 + i + i + 1 == num:
        #        return [i - 1, i, i + 1]
        # return []
        w = int(num / 3)
        if w - 1 + w + w + 1 == num:
            return [w - 1, w, w + 1]
        return []


num = 33
s = Solution()
print(s.sumOfThree(num))
