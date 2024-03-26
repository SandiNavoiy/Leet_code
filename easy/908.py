class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        ''''''
        if (max(nums) -k) - (min(nums) +k) < 0:
            return 0
        return (max(nums) -k) - (min(nums) +k)
nums = [1,3,6]
k = 2
s = Solution()
print(s.smallestRangeI(nums, k))