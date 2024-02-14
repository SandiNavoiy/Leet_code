class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        """"""
        new = 0
        while len(nums) > 1:
            x = nums.pop(0)
            y = nums.pop(-1)
            z = int(str(x) + str(y))
            new += z
        if len(nums) == 1:
            new = new + nums[0]
        return new


nums = [5, 14, 13, 8, 12]
s = Solution()
print(s.findTheArrayConcVal(nums))
# 673
