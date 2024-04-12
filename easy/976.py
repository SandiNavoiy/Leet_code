class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        ''''''
        ss = 0
        nums.sort(reverse=True)


        for i in range(len(nums)-2):
            if nums[i] < nums[i +1] + nums[i +2]:
                if nums[i] + nums[i +1] + nums[i +2] > ss:
                    ss = nums[i] + nums[i +1] + nums[i +2]
        return ss
nums = [3,2,3,4]
s = Solution()
print(s.largestPerimeter(nums))