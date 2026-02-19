class Solution:
    def alternatingSum(self, nums) -> int:
        rez = 0
        for i in range(len(nums)):
            if i%2 == 0:
                rez += nums[i]
            else:
                rez -= nums[i]

        return rez

