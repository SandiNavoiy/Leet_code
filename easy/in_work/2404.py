class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        """"""
        if len(nums) == 1:
            return nums[0]
        x = 1
        y = []
        for i in nums:
            if nums.count(i) > x and i % 2 == 0:
                x = nums.count(i)

                y.append(i)
        if x == 1:
            return -1
        else:
            return y


nums = [2, 10000, 10000, 10000, 2]
s = Solution()
print(s.mostFrequentEven(nums))


hjhj = " dsgdfhfgj"
hjhj.re
