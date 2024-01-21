class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """"""
        pol = []
        otr = []
        new = []
        for i in nums:
            if i > 0:
                pol.append(i)
            else:
                otr.append(i)
        for i in range(len(pol)):
            new.append(pol[i])
            new.append(otr[i])
        return new


nums = [3, 1, -2, -5, 2, -4]
s = Solution()
print(s.rearrangeArray(nums))
