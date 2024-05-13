class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """"""
        if len(nums) == 1:
            return [str(nums[0])]
        new = []
        temp = []
        rez = []
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1] - 1 and i < len(nums) - 2:
                temp.append(nums[i])
            elif i == len(nums) - 2:
                if nums[i] == nums[i + 1] - 1:
                    temp.append(nums[i])
                    temp.append(nums[i + 1])
                    new.append(temp)
                else:
                    temp.append(nums[i])
                    new.append(temp)
                    temp = []
                    temp.append(nums[i + 1])
                    new.append(temp)
            else:
                temp.append(nums[i])
                new.append(temp)
                temp = []
        for i in new:
            if i[0] != i[-1]:
                x = str(i[0]) + "->" + str(i[-1])
                rez.append(x)
            else:
                rez.append(str(i[0]))

        return rez


nums = [-1]
s = Solution()
print(s.summaryRanges(nums))
