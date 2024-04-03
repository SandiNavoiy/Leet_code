class Solution:
    def triangleType(self, nums: list[int]) -> str:
        """"""
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if (
            nums[0] + nums[1] > nums[2]
            and nums[0] + nums[2] > nums[1]
            and nums[2] + nums[1] > nums[0]
        ):
            if nums[0] == nums[1] or nums[2] == nums[1] or nums[0] == nums[2]:
                return "isosceles"
            else:
                return "scalene"
        return "none"


nums = [3, 4, 5]
s = Solution()
print(s.triangleType(nums))
