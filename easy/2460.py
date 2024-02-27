class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        ''''''
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] *2
                nums[i+1] = 0
        nums1 = []
        nums2 = []
        for i in range(len(nums)):
            if nums[i] != 0:
                nums1.append(nums[i])
            else:
                nums2.append(0)


        return nums1 + nums2
nums = [1,2,2,1,1,0]
s = Solution()
print(s.applyOperations(nums))