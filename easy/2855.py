class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        i=nums.index(max(nums))
        nums=nums[i+1:]+nums[:i+1]
        for j in range(len(nums)-1):
            if nums[j+1]<nums[j]:
                return -1
        return len(nums)-i-1


nums = [3, 4, 5, 1, 2]
s = Solution()
print(s.minimumRightShifts(nums))
