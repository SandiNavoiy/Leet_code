class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        """"""
        odnoz = []
        dvuz = []
        for i in nums:
            if i >= 10:
                dvuz.append(i)
            else:
                odnoz.append(i)

        if sum(dvuz) == sum(odnoz):
            return False
        return True


nums = [1, 2, 3, 4, 10]
s = Solution()
print(s.canAliceWin(nums))
